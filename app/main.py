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

    return {"prediction": prediction, "result": result, "confidence": round(confidence, 6)}

# Metrics Endpoint
@app.get("/metrics")
async def metrics():
    """
    Returns metrics computed on the held-out test set at /model/diabetes_test.npz
    (expects arrays saved as X and y).
    Falls back to precomputed metrics at /model/diabetes_metrics.pkl
    if the test set isn't available.
    """
    try:
        from sklearn.metrics import (
            accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
        )

        # Preferred: compute from saved test set
        try:
            data = np.load("/model/diabetes_test.npz")
            X_test, y_test = data["X"], data["y"]

            y_pred = model.predict(X_test)

            # Compute ROC AUC from probabilities if possible; otherwise try decision_function
            roc_auc = None
            if hasattr(model, "predict_proba"):
                y_prob = model.predict_proba(X_test)[:, 1]
                roc_auc = roc_auc_score(y_test, y_prob)
            elif hasattr(model, "decision_function"):
                scores = model.decision_function(X_test)
                roc_auc = roc_auc_score(y_test, scores)

            return {
                "accuracy": float(accuracy_score(y_test, y_pred)),
                "precision": float(precision_score(y_test, y_pred, zero_division=0)),
                "recall": float(recall_score(y_test, y_pred, zero_division=0)),
                "f1_score": float(f1_score(y_test, y_pred, zero_division=0)),
                "roc_auc": float(roc_auc) if roc_auc is not None else None,
            }

        except Exception as test_err:
            # Fallback: load precomputed metrics
            try:
                metrics_data = joblib.load("/model/diabetes_metrics.pkl")
                # ensure plain floats
                return {k: float(v) if v is not None else None for k, v in metrics_data.items()}
            except Exception as metrics_err:
                return {
                    "error": "Metrics not available on server.",
                    "details": {
                        "test_set_error": str(test_err),
                        "metrics_file_error": str(metrics_err),
                    },
                }
    except Exception as e:
        return {"error": f"Unexpected error computing metrics: {e}"}
