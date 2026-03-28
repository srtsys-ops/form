import pickle
import streamlit as st

diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

input_data = [[
    6,178,90,35,220,34.60,1.450,62
]]

diab_prediction = diabetes_model.predict(input_data)

# Display prediction result
if diab_prediction[0] == 1:
    st.error("🔴 The person is Diabetic")
else:
    st.success("🟢 The person is not Diabetic")
