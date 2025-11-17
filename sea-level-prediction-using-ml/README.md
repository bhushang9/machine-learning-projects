# 🌊 Sea Level Prediction Using Prophet

A time-series forecasting project that uses historical Monthly Mean Sea Level (MSL) data from NOAA to analyze past trends and predict future sea levels using the **Prophet** model.

---

## 📌 Project Overview

This project processes NOAA tide-gauge data to study long-term sea level changes.  
Using the Prophet forecasting model, it predicts future sea level trends and evaluates model accuracy using MAE and SMAPE.  
Long-term projections up to **2100** are also generated.

---

## 🔍 Objectives

- Download and clean NOAA sea level data  
- Explore and visualize historical sea level trends  
- Build a forecasting model using Prophet  
- Evaluate model performance (MAE & SMAPE)  
- Generate short-term and long-term predictions  
- Compare results with NOAA’s regional sea-level scenarios  

---

## 🧪 Tools & Technologies

- Python  
- Google Colab / Jupyter Notebook  
- Pandas, NumPy, Matplotlib  
- Prophet (Meta)  
- NOAA Sea Level Trends Dataset  

---

## 📥 Data Source

NOAA Sea Level Trends (tide-gauge data).  
Choose any station with at least **100+ years** of data.

Data exported from:

- NOAA Relative Sea Level Trends  
- NOAA U.S. RSL Linear Trends & 95% Confidence Intervals  

---

## 🧹 Data Preprocessing

- Removed extra header rows  
- Cleaned column names  
- Combined **Year + Month** → `ds` column (Prophet format)  
- Converted `ds` to datetime index  
- Visualized monthly values + 12-month rolling averages  
- Train/Test split:
  - **Train:** 1975–2000  
  - **Test:** 2000–2025  

---

## 📈 Modeling (Prophet)

- Fitted Prophet model on training data  
- Forecasted values for test period  
- Generated future predictions up to **2100**  
- Visualized forecasts with uncertainty intervals  

---

## 📊 Evaluation Metrics

### **Mean Absolute Error (MAE):**  
Measures average prediction error.

### **Symmetric Mean Absolute Percentage Error (SMAPE):**  
Percentage-based accuracy for balanced evaluation.

---

## 🌍 Key Questions Answered

- Has sea level rise accelerated over time?  
- How accurate is Prophet for near-term predictions?  
- When does the model underpredict or overpredict?  
- How do long-term forecasts compare with NOAA projections?  

---

## 📦 Project Type

**Machine Learning — Time Series Forecasting (Environmental Data Science)**

---


