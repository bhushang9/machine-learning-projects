import streamlit as st
import pandas as pd
import joblib
import numpy as np

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Segmentation Prediction")
st.write("Enter customer details to predict their segment.")

age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Annual Income", min_value=0, max_value=2000000, value=50000)
total_spending = st.number_input("Total Spending (sum of purchases)", min_value=0, max_value=5000, value=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=10)
num_web_visits = st.number_input("Number of Web Visits p/m", min_value=0, max_value=50, value=30)  
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_Spending": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})

input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)
    st.success(f"The predicted customer segment is: Cluster {cluster[0]}")