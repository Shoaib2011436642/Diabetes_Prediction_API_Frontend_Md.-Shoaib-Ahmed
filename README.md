
# Diabetes Prediction API Frontend  
### By Md. Shoaib Ahmed

### **Live Render Link (Backend API):**  
https://diabetes-prediction-api-frontend-md.onrender.com/docs

### **Live Frontend Link (Streamlit):**
https://diabetespredictionapifrontendmd-shoaib-ahmed-dqtj9yy42va3abybw.streamlit.app/

---

### **Project Overview**

This project aims to develop a **Diabetes Prediction System** using machine learning models. The model is trained using the **Pima Indians Diabetes Dataset** with multiple classifiers such as **Logistic Regression**, **Random Forest**, **Support Vector Machine (SVM)**, **Decision Tree**, and **K-Nearest Neighbors (KNN)**. The best-performing model, **Decision Tree**, is deployed using **FastAPI** and containerized using **Docker**. The backend is hosted on **Render**, and the frontend is built using **Streamlit**.

---

### **Technologies Used**

- **FastAPI**: For building the backend web API with async endpoints.
- **Streamlit**: For building the interactive frontend web application.
- **scikit-learn**: For building and training the machine learning models.
- **joblib**: For saving and loading the trained model.
- **Docker**: For containerizing the FastAPI app.
- **Render**: For deploying the FastAPI app and making the API accessible.
- **uvicorn**: For running the FastAPI app in production.

---

### **Purpose of the Project**

This project provides an easy-to-use tool for **predicting diabetes** based on key health metrics such as glucose levels, BMI, age, and more. The goal is to assist healthcare professionals by providing a quick, reliable prediction of whether a patient is diabetic or not, based on their health data.

---

### **How to Run Locally (Using Docker Desktop)**

1. Open **PowerShell** or **Terminal** in your project folder.

2. Build and run the Docker container:
   ```bash
   docker-compose build
   docker-compose up
   ```

3. Open the app in your browser:
   - Go to `http://localhost:8000/docs` to interact with the API.

---

### **Deployment on Render**

The application is deployed on **Render** using Docker. The deployment steps include:

1. **Create a Render web service** and link it to the GitHub repository.
2. **Configure Docker** by setting the build context to `.` (root directory) and specifying the Dockerfile.
3. **Deploy** the application using Render’s **continuous deployment** feature, which automatically rebuilds the app whenever changes are pushed to the GitHub repository.

The app is live and accessible via **Render's provided URL**, where you can interact with the API through Swagger UI.

---

### **Frontend Deployment with Streamlit**

The **Streamlit** frontend is also deployed separately. It connects to the backend **/predict** API endpoint on Render to make real-time predictions. 

Steps for Streamlit Deployment:
1. **Build the frontend with Streamlit** to allow users to input health metrics like age, BMI, glucose, etc.
2. **Send the user input data** to the `/predict` endpoint on Render via a POST request.
3. **Display the result** from the backend (whether the user is diabetic or not) along with the confidence score.

The Streamlit app can be accessed through a public link, allowing users to interact with the diabetes prediction system directly.

---

### **Expected Result**

The app predicts whether a person has diabetes based on the following input features:

- Pregnancies
- Glucose level
- Blood Pressure
- Skin Thickness
- Insulin levels
- BMI
- Diabetes Pedigree Function
- Age

The result is returned as a **binary classification**:

- **0**: Not Diabetic
- **1**: Diabetic

The app also provides a **confidence score** for each prediction.

---

### **Future Enhancements**

- Improve model accuracy and try other classification algorithms.
- Integrate real-time data collection for continuous monitoring.
- Add a feature to allow users to upload data files (e.g., CSV) for batch predictions.

---
