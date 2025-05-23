import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page settings
st.set_page_config(page_title="Real Estate Analytics", layout="wide")

st.title('🏙️ Gurgaon Real Estate Analytics Dashboard')

# Load data
new_df = pd.read_csv('data_viz1.csv')
feature_text = pickle.load(open('feature_text.pkl', 'rb'))

# Grouped sector data
group_df = new_df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

# 🗺️ Sector Price per Sqft GeoMap
st.header('📍 Sector-wise Price per Sqft GeoMap')
fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    width=1200,
    height=700,
    hover_name=group_df.index
)
st.plotly_chart(fig, use_container_width=True)

# ☁️ Wordcloud of Features
st.header('🔠 Most Common Property Features (Wordcloud)')
wordcloud = WordCloud(
    width=800, height=800,
    background_color='black',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

fig_wc, ax_wc = plt.subplots(figsize=(8, 8))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis("off")
st.pyplot(fig_wc)

# 📐 Area vs Price by Property Type
st.header('📏 Area vs Price (Choose Property Type)')
property_type = st.selectbox('Select Property Type:', ['flat', 'house'])

filtered_df = new_df[new_df['property_type'] == property_type]
fig1 = px.scatter(
    filtered_df, x="built_up_area", y="price", color="bedRoom",
    title=f"Area vs Price for {property_type.capitalize()}s"
)
st.plotly_chart(fig1, use_container_width=True)

# Bedroom Distribution by Sector
st.header('🛏️ BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'Overall')
selected_sector = st.selectbox('Select Sector:', sector_options)

if selected_sector == 'Overall':
    pie_df = new_df
else:
    pie_df = new_df[new_df['sector'] == selected_sector]

fig2 = px.pie(pie_df, names='bedRoom', title=f"BHK Distribution - {selected_sector}")
st.plotly_chart(fig2, use_container_width=True)

# Side-by-Side BHK Price Comparison
st.header('💸 BHK Price Distribution (Box Plot)')
fig3 = px.box(
    new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price',
    title='Price Range by BHK (up to 4 BHK)'
)
st.plotly_chart(fig3, use_container_width=True)

# Distribution of Price by Property Type
st.header('🏘️ Price Distribution: House vs Flat')
fig4, ax4 = plt.subplots(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='House', kde=True, color='blue')
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', kde=True, color='green')
plt.legend()
st.pyplot(fig4)
