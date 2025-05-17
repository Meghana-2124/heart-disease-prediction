import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the saved model
with open('heart_disease_model.sav', 'rb') as f:
    loaded_model = pickle.load(f)

# Prediction function
def heart_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'

def heart_prediction_page():
    st.title("Choose the Algorithm")
    algorithm = st.selectbox("Select the prediction algorithm", ["Logistic Regression", "Decision Tree", "Random Forest", "SVM"])

    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://globetechcdn.com/mobile_hospimedica/images/stories/articles/article_images/2022-07-15/SDD-294793891.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True)

    st.title('Heart Disease Prediction Web App')
    st.subheader("**Please enter the following information:**")

    age = st.number_input('Age (years)', min_value=0, max_value=120, value=30)
    sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3], format_func=lambda x: {0: 'Typical Angina', 1: 'Atypical Angina', 2: 'Non-Anginal Pain', 3: 'Asymptomatic'}.get(x, 'Unknown'))
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
    chol = st.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    restecg = st.selectbox('Resting ECG', options=[0, 1, 2], format_func=lambda x: {0: 'Normal', 1: 'ST-T Abnormality', 2: 'Left Ventricular Hypertrophy'}.get(x, 'Unknown'))
    thalach = st.number_input('Max Heart Rate Achieved', min_value=0, max_value=250, value=150)
    exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=10.0, value=1.0, format="%.1f")
    slope = st.selectbox('Slope of Peak ST', options=[0, 1, 2], format_func=lambda x: {0: 'Upsloping', 1: 'Flat', 2: 'Downsloping'}.get(x, 'Unknown'))
    ca = st.selectbox('Number of Major Vessels (0-3)', options=[0, 1, 2, 3])
    thal = st.selectbox('Thalassemia', options=[0, 1, 2, 3], format_func=lambda x: {0: 'Normal', 1: 'Fixed Defect', 2: 'Reversible Defect', 3: 'Unknown'}.get(x, 'Unknown'))

    # Prediction
    if st.button('Heart Disease Test Result'):
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        diagnosis = heart_prediction(input_data)
        st.success(diagnosis)
