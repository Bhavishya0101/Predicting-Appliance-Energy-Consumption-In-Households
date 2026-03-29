import streamlit as st
import pandas as pd
import joblib

# Load model + feature names
model, feature_names = joblib.load("energy_model2.pkl")

st.title("⚡ Energy Consumption Predictor")

# --- USER INPUTS ---
T1 = st.number_input("T1", value=20.0)
RH_1 = st.number_input("RH_1", value=50.0)
hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

# --- CREATE FULL INPUT ---
input_dict = {}

# Fill ALL features
for col in feature_names:
    input_dict[col] = 0   # default value

# Replace important ones
input_dict["T1"] = T1
input_dict["RH_1"] = RH_1

if "hour" in feature_names:
    input_dict["hour"] = hour
if "day" in feature_names:
    input_dict["day"] = day
if "month" in feature_names:
    input_dict["month"] = month

# Convert to DataFrame
input_data = pd.DataFrame([input_dict])

# --- PREDICT ---
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        st.success(f"⚡ Energy Consumption: {prediction[0]:.2f} Wh")
    except Exception as e:
        st.error(f"Error: {e}")
