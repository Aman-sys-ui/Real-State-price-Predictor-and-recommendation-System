import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib

# Load model
with open('pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

# Optional: Load reference dataframe (for column order or preprocessing if needed)
with open('df.pkl', 'rb') as file:
    df = pickle.load(file)
# st.dataframe(df)

st.header("🔮 Price Prediction")

# fields
property_type = st.selectbox("Property Type", ['flat',  'independent house'])
sector = st.selectbox('sector' ,sorted(df['sector'].unique().tolist()))
bedroom = float(st.selectbox("Bedrooms", sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox("Bathrooms", sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox("Balcony", sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox("Age of Property", sorted(df['agePossession'].unique().tolist()))
area = float(st.number_input("Built-Up Area (sq.ft)", 200, 10000, 1000))
servant = float(st.radio("Servant Room", [0.0, 1]))
store = float(st.radio("Store Room", [0.0, 1]))
furnish = st.selectbox("Furnishing Type", sorted(df['furnishing_type'].unique().tolist()))
luxury = st.selectbox("Luxury Category", sorted(df['luxury_category'].unique().tolist()))
floor_cat = st.selectbox("Floor Category", sorted(df['floor_category'].unique().tolist()))

# Prediction
if st.button("Predict Price"):
    data = [[property_type ,sector ,bedroom , bathroom ,balcony , property_age ,area ,servant ,store,furnish ,luxury,floor_cat]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)


    try:
        prediction = model.predict(one_df)[0]
        st.success(f"🏷️ Estimated Price: ₹{prediction:.2f} Cr")
    except Exception as e:
        st.error(f"❌ Prediction Failed: {e}")
