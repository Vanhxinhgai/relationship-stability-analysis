# Relationship Stability Analysis and Prediction

## Overview
This project analyzes relationship stability using the Divorce Prediction dataset.  
The goal is to perform Exploratory Data Analysis (EDA), identify important factors related to relationship status, and build machine learning models for prediction.

## Dataset
- Source: Kaggle Divorce Prediction Dataset
- Main file: `divorce_data.csv`
- Reference file: `reference.tsv`
- Target variable: `Divorce`
  - 0: Stable / No Divorce
  - 1: Divorce / Unstable

## Research Questions
1. Which features are most strongly correlated with relationship status?
2. How do stable and unstable relationship groups differ in important features?
3. How accurately can machine learning models classify relationship status?

## Methods
- Data loading and cleaning
- Duplicate checking and removal
- Exploratory Data Analysis
- Correlation analysis
- Mean score comparison between groups
- Logistic Regression
- Random Forest

## Results
- Logistic Regression Accuracy: 100%
- Random Forest Accuracy: 97.06%

## Prototype
A simple Python Streamlit prototype was developed to simulate a survey-based relationship stability prediction system.

To run the app:

```bash
streamlit run app.py
