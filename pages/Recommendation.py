import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Streamlit page configuration
st.set_page_config(page_title="🏡 Apartment Recommender", layout="wide")
st.title("🏙️ Gurgaon Real Estate Recommender System")

# Load data
location_df = pickle.load(open('cleaned_location_df.pkl', 'rb'))
location_df.set_index('PropertyName', inplace=True)

cosine_sim1 = pickle.load(open('cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('cosine_sim3.pkl', 'rb'))

# Recommender function
def recommend_properties_with_scores(property_name, top_n=5):
    # Weighted combination of cosine similarity matrices
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1.0 * cosine_sim3

    if property_name not in location_df.index:
        return pd.DataFrame(columns=['PropertyName', 'SimilarityScore'])

    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    return pd.DataFrame({
        '🏘️ Property Name': top_properties,
        '🔍 Similarity Score': [round(score, 3) for score in top_scores]
    })

# --------------------------------------------
# SECTION 1: Location-Based Search
# --------------------------------------------
st.subheader("📍 Location-Based Property Search")
selected_location = st.selectbox("Choose a location:", sorted(location_df.columns.to_list()))
radius = st.number_input("Enter radius (in kms):", min_value=1, value=3)

if st.button("🔎 Search Nearby Properties"):
    try:
        result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
        if result_ser.empty:
            st.warning("No properties found within this radius.")
        else:
            st.success(f"Found {len(result_ser)} properties:")
            for key, value in result_ser.items():
                st.markdown(f"- **{key}** — 🛣️ {round(value/1000, 2)} km away")
    except Exception as e:
        st.error(f"Error: {e}")


# SECTION 2: Content-Based Recommendations

st.subheader("🤝 Similar Apartment Recommendations")
selected_appartment = st.selectbox("Choose an apartment:", sorted(location_df.index.to_list()))

if st.button("💡 Recommend Similar Apartments"):
    with st.spinner("Fetching recommendations..."):
        recommendation_df = recommend_properties_with_scores(selected_appartment)

        if recommendation_df.empty:
            st.warning("No similar properties found.")
        else:
            st.dataframe(recommendation_df)
