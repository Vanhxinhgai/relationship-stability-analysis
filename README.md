# Relationship Stability Analysis and Prediction

## 1. Introduction
This project analyzes relationship stability using the Divorce Prediction dataset.

## 2. Objectives
- Analyze important factors related to relationship status.
- Compare stable and unstable groups.
- Build machine learning models for prediction.

## 3. Research Questions
1. Which features are most strongly correlated with relationship status?
2. How do stable and unstable groups differ in important features?
3. How accurately can machine learning models classify relationship status?

## 4. Dataset
- Source: Kaggle Divorce Prediction Dataset
- 170 samples
- 54 survey questions
- Target variable: Divorce
  - 0: Stable / No Divorce
  - 1: Divorce / Unstable

## 5. Methodology
- Data cleaning
- Duplicate removal
- Exploratory Data Analysis
- Correlation analysis
- Mean score comparison
- Logistic Regression
- Random Forest

## 6. Results
- Logistic Regression Accuracy: 100%
- Random Forest Accuracy: 97.06%
- Top correlated features: Q40, Q17, Q19, Q18, Q11

## 7. Prototype
A Python Streamlit prototype was developed to simulate the real-world application.

Run the app:

```bash
streamlit run app.py
