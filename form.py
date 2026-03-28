import pickle
import streamlit as st

diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# input_data = [[
#     6,178,90,35,220,34.60,1.450,62
# ]]

# input_data = [[
#     3,126,88,41,235,39.30,0.704,27
# ]]

# Pregnancies = 3
# Glucose = 126
# BloodPressure = 88
# SkinThickness = 41
# Insulin = 235
# BMI = 39.30
# DiabetesPedigreeFunction = 0.704
# Age = 27

Pregnancies = 6
Glucose = 178
BloodPressure = 98
SkinThickness = 35
Insulin = 220
BMI = 34.6
DiabetesPedigreeFunction = 1.45
Age = 62



input_data = [[
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
]]

diab_prediction = diabetes_model.predict(input_data)

# Display prediction result
if diab_prediction[0] == 1:
    st.error("🔴 The person is Diabetic")
else:
    st.success("🟢 The person is not Diabetic")
