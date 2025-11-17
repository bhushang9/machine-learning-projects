🌊 Sea Level Prediction Using Prophet

A time-series forecasting project using historical Monthly Mean Sea Level (MSL) data from NOAA to predict future sea level trends.

📌 Project Overview

This project uses NOAA tide-gauge data to understand how sea levels have changed over time and to predict future sea levels using the Prophet forecasting model. The dataset is cleaned, visualized, modeled, and evaluated using multiple error metrics (MAE and SMAPE). A long-term projection up to the year 2100 is also generated.

🔍 Objectives

Download and prepare long-term NOAA sea level data

Explore and visualize historical sea level trends

Build a forecasting model using Prophet

Evaluate model performance on unseen test data

Predict future sea levels (short-term & long-term)

Compare predictions with NOAA’s regional sea-level scenarios

🧪 Tools & Technologies

Python

Google Colab / Jupyter Notebook

Pandas, NumPy, Matplotlib

Prophet (Meta)

NOAA Sea Level Trends Dataset

📥 Data Source

NOAA Sea Level Trends:
You can select any tide-gauge station with at least 100+ years of data.
CSV exported from:

NOAA Relative Sea Level Trends

NOAA U.S. RSL Linear Trends & Confidence Intervals

🧹 Data Preprocessing

Removed unnecessary header rows

Cleaned column names

Combined Year and Month into Prophet-compatible ds column

Set ds as datetime index

Visualized monthly values and rolling averages

Split dataset into Train (1975–2000) and Test (2000–2025)

📈 Modeling

The project uses the Prophet model to forecast Monthly Mean Sea Levels:

Steps include:

Fitting the model on training data

Forecasting test data

Generating future predictions until 2100

Visualizing forecast trend + uncertainty intervals

📊 Evaluation Metrics

The model is evaluated using:

✔ Mean Absolute Error (MAE)

Shows the average size of prediction errors.

✔ Symmetric Mean Absolute Percentage Error (SMAPE)

Shows percentage-based prediction accuracy.

🌍 Key Questions Answered

Has sea level rise accelerated over the past century?

How well does Prophet predict near-term sea level changes?

Where does the model underpredict or overpredict?

How do long-term forecasts compare to NOAA scientific scenarios?
