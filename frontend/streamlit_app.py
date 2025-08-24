import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="Diabetes Prediction", page_icon="⚕️")

# Your online image URL
BG_URL = "https://images.pexels.com/photos/6942015/pexels-photo-6942015.jpeg"

# Inject CSS: gradient overlay + background image
st.markdown(
    f"""
    <style>
    /* Main page background */
    [data-testid="stAppViewContainer"] {{
        background: 
            linear-gradient(rgba(0,0,0,0.50), rgba(0,0,0,0.50)),  /* overlay */
            url('{BG_URL}') no-repeat center center / cover fixed;
    }}

    /* Make header transparent so background shows through */
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    /* Optional: match sidebar with the same image + overlay */
    [data-testid="stSidebar"] > div:first-child {{
        background: 
            linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)),
            url('{BG_URL}') no-repeat center center / cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("Diabetes Prediction App Using Random Forest Model")
st.subheader("Authored By: Md. Shoaib Ahmed")
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
    response = requests.post("https://diabetes-prediction-api-frontend-md-59ys.onrender.com/predict", json=data)

    # Check if the response was successful
    if response.status_code == 200:
        prediction = response.json()

        # Ensure that the response is well-structured
        st.write("Prediction Response:", prediction)  # Inspect the response

        # Accessing prediction and confidence
        result = prediction.get('result', 'Unknown')
        confidence = prediction.get('confidence', 0.0)

        # Display results
        st.write(f"Prediction: {result}")
        st.write(f"Confidence: {confidence*100}%")
    else:
        st.write("Error occurred while fetching prediction.")
