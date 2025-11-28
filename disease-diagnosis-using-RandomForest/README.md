# 🩺 Disease Diagnosis Using Random Forest

This project builds a disease prediction system using symptom data. It trains a Random Forest model, checks how well it performs, visualizes results, and includes a feature to manually predict diseases through user input.

---

## 📁 Dataset
Dataset: https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning?select=Training.csv

Files used:
Training.csv — for model training
Testing.csv — for evaluating the model
One unnecessary column (Unnamed: 133) is removed during processing.

---

## 🎯 Key features 

- Checks and removes any unnecessary columns
- Trains the model using Random Forest
- Finds the best settings using Grid Search
- Tests the model on the testing dataset
- Shows accuracy, report, and confusion heatmap
- Allows users to manually enter symptoms (0 or 1) to get a prediction

---

## 🛠️ Tech Stack

- Pandas – for handling the dataset
- NumPy
- Matplotlib & Seaborn – for visualizations
- Scikit-learn – for model training, tuning, and evaluation
- Random Forest Classifier
- GridSearchCV

---

## 📌 Conclusion

The model gives quick disease predictions based on symptoms and shows how machine learning can support basic diagnosis.

---
