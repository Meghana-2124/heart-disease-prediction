# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:43:33 2024

@author: HP
"""

import numpy as np 
import pickle
import streamlit as st
from PIL import Image

# Loading the saved model
loaded_model = pickle.load(open('C:/Users\HP\Desktop\test/heart_disease_model.sav', 'rb'))


# Creating a function for prediction
def heart_prediction(input_data):
    # Change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # Reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make the prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'

def heart_prediction_page():
    st.title("Choose the Algorithm")
    
    algorithm = st.selectbox("Select the prediction algorithm", ["Logistic Regression", "Decision Tree", "Random Forest","SVM"])
    
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
    # Giving a title
    st.title('Heart Disease Prediction Web App')
    
    st.subheader("**Please enter the following information:**")
    
    
    age = st.number_input('Age (years)', min_value=0, max_value=120, value=30)
    
    sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    st.write("0 = Female, 1 = Male")
    
    cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3], format_func=lambda x: {
        0: 'Typical Angina',
        1: 'Atypical Angina',
        2: 'Non-Anginal Pain',
        3: 'Asymptomatic'
    }.get(x, 'Unknown'))  # Use get to avoid KeyError
    st.write("0 = Typical Angina, 1 = Atypical Angina, 2 = Non-Anginal Pain, 3 = Asymptomatic")
    
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
    
    chol = st.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200)
    
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    st.write("0 = No, 1 = Yes")
    
    restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2], format_func=lambda x: {
        0: 'Normal',
        1: 'Having ST-T Wave Abnormality',
        2: 'Showing Left Ventricular Hypertrophy'
    }.get(x, 'Unknown'))  # Use get to avoid KeyError
    st.write("0 = Normal, 1 = ST-T Wave Abnormality, 2 = Left Ventricular Hypertrophy")
    
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, value=150)
    
    exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    st.write("0 = No, 1 = Yes")
    
    oldpeak = st.number_input('Oldpeak (depression induced by exercise relative to rest)', min_value=0.0, max_value=10.0, value=1.0, format="%.1f")
    
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2], format_func=lambda x: {
        0: 'Upsloping',
        1: 'Flat',
        2: 'Downsloping'
    }.get(x, 'Unknown'))  # Use get to avoid KeyError
    st.write("0 = Upsloping, 1 = Flat, 2 = Downsloping")
    
    ca = st.selectbox('Number of Major Vessels (0-3)', options=[0, 1, 2, 3], format_func=lambda x: {
        0: 'No Vessels',
        1: '1 Vessel',
        2: '2 Vessels',
        3: '3 Vessels'
    }.get(x, 'Unknown'))  # Use get to avoid KeyError
    st.write("0 = No Vessels, 1= 1 vessels, 2 = 2 vessels, 3 = 3 vessels")
    
    thal = st.selectbox('Thalassemia', options=[0, 1, 2, 3], format_func=lambda x: {
    0: 'Normal',
    1: 'Fixed Defect',
    2: 'Reversible Defect',
    3: 'Unknown'  # You can add a description for 3 if needed
    }.get(x, 'Unknown'))  # Use get to avoid KeyError
    st.write("0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect, 3 = Unknown")
    
    # Code for prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Collect input data into a list
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        diagnosis = heart_prediction(input_data)
    
    st.success(diagnosis)
