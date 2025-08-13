import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="Diabetes Prediction", page_icon="⚕️")

# Title and description
st.title("Diabetes Prediction App")
st.write("Enter the values below to predict whether a patient has diabetes or not.")

# Input fields for user data
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

# Button to make prediction
if st.button("Predict"):
    data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree_function,
        "Age": age
    }
    
    # Send POST request to the FastAPI backend
    response = requests.post("https://diabetes-prediction-api-frontend-md.onrender.com/docs/predict", json=data)
    prediction = response.json()

    # Display results
    st.write(f"Prediction: {prediction['result']}")
    st.write(f"Confidence: {prediction['confidence']*100}%")
