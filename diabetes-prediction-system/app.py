import streamlit as st
import numpy as np
import pickle

# load model and scaler
model = pickle.load(open('final_rf_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# app title
st.title("Diabetes Prediction App")
st.write("Enter your clinical values to check the diabetes risk prediction.")

# input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=0)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.0)
age = st.number_input("Age", min_value=1, max_value=100, value=1)


# prediction button
if st.button("Predict"):
    # prepare input
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])

    # scale
    scaled_input = scaler.transform(input_data)

    # predict
    prediction = model.predict(scaled_input)

    # result
    if prediction[0] == 1:
        st.error("⚠️ High risk of Diabetes")
    else:
        st.success("✅ Low risk of Diabetes")
