import streamlit as st
import pandas as pd
import joblib

# Load model + feature names
model, feature_names = joblib.load("energy_model2.pkl")

st.set_page_config(page_title="Energy Predictor", layout="centered")

st.title("⚡ Appliance Energy Consumption Predictor")
st.write("Enter values to predict energy consumption")

# --- INPUTS ---
T1 = st.number_input("Kitchen Temperature (T1)", value=20.0)
RH_1 = st.number_input("Kitchen Humidity (RH_1)", value=50.0)

T2 = st.number_input("Living Room Temperature (T2)", value=20.0)
RH_2 = st.number_input("Living Room Humidity (RH_2)", value=50.0)

T3 = st.number_input("Laundry Temperature (T3)", value=20.0)
RH_3 = st.number_input("Laundry Humidity (RH_3)", value=50.0)

hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

# --- CREATE INPUT DATA (FIXED: 1 ROW) ---
input_dict = {col: 0 for col in feature_names}

# Fill user inputs
if "T1" in input_dict:
    input_dict["T1"] = T1
if "RH_1" in input_dict:
    input_dict["RH_1"] = RH_1
if "T2" in input_dict:
    input_dict["T2"] = T2
if "RH_2" in input_dict:
    input_dict["RH_2"] = RH_2
if "T3" in input_dict:
    input_dict["T3"] = T3
if "RH_3" in input_dict:
    input_dict["RH_3"] = RH_3
if "hour" in input_dict:
    input_dict["hour"] = hour
if "day" in input_dict:
    input_dict["day"] = day
if "month" in input_dict:
    input_dict["month"] = month

# Convert to DataFrame (IMPORTANT: must have 1 row)
input_data = pd.DataFrame([input_dict])

# --- PREDICTION ---
if st.button("Predict Energy Consumption"):
    try:
        prediction = model.predict(input_data)
        st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.2f} Wh")
    except Exception as e:
        st.error(f"Error: {e}")
