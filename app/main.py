from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model
try:
    model = joblib.load('/model/diabetes_model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

# Request Body for Prediction
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Health Endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}

# Prediction Endpoint
@app.post("/predict")
async def predict(patient: PatientData):
    data = np.array([[patient.Pregnancies, patient.Glucose, patient.BloodPressure, patient.SkinThickness, 
                      patient.Insulin, patient.BMI, patient.DiabetesPedigreeFunction, patient.Age]])
    prediction = model.predict(data)
    confidence = model.predict_proba(data)[0][prediction[0]]
    
    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

    # Convert numpy.int64 to a native Python int
    prediction = int(prediction[0])
    confidence = float(confidence)

    return {"prediction": prediction, "result": result, "confidence": round(confidence, 2)}

# Metrics Endpoint
@app.get("/metrics")
async def metrics():
    # Return a sample of classification metrics from the test set
    return {
        "accuracy": 0.77,
        "precision": 0.67,
        "recall": 0.67,
        "f1_score": 0.67,
        "roc_auc": 0.75
    }
