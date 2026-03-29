import streamlit as st
import pandas as pd
import joblib

# Load model, features, and mean values
model, feature_names, feature_means = joblib.load("energy_model.pkl")

st.title("⚡ Appliance Energy Consumption Predictor")

# --- USER INPUTS ---
T1 = st.number_input("T1 (Kitchen Temp)", value=20.0)
RH_1 = st.number_input("RH_1 (Kitchen Humidity)", value=50.0)
hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

# --- CREATE FULL INPUT (KEY FIX) ---
# Start with mean values (so no missing features)
input_dict = feature_means.to_dict()

# Replace with user inputs
input_dict["T1"] = T1
input_dict["RH_1"] = RH_1

if "hour" in input_dict:
    input_dict["hour"] = hour
if "day" in input_dict:
    input_dict["day"] = day
if "month" in input_dict:
    input_dict["month"] = month

# Convert to DataFrame with correct column order
input_data = pd.DataFrame([input_dict])[feature_names]

# --- PREDICTION ---
if st.button("Predict Energy Consumption"):
    try:
        prediction = model.predict(input_data)
        st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.2f} Wh")
    except Exception as e:
        st.error(f"Error: {e}")
