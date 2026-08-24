# Soil Fertility Prediction Using Machine Learning

## Project Overview

This project presents a machine learning based system for predicting soil fertility using soil nutrient parameters. The system analyzes Nitrogen (N), Phosphorus (P), Potassium (K), and pH values and predicts the fertility level of the soil.

Based on the predicted fertility level, the system also provides a suitable crop recommendation.

## Objectives

- Analyze important soil nutrient parameters.
- Predict soil fertility using Machine Learning.
- Classify soil into Low, Medium, and High fertility levels.
- Recommend suitable crops based on predicted fertility.
- Develop a user-friendly dashboard for real-time prediction.
- Deploy the trained model for demonstration.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Joblib
- Streamlit
- Google Colab
- GitHub

## Input Parameters

The system uses:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- pH

## Machine Learning Model

A Random Forest Classifier is used for soil fertility classification.

The trained model is saved as:

`soil_model.pkl`

## Project Workflow

Dataset
↓
Data Preprocessing
↓
Feature Selection
↓
Fertility Classification
↓
Random Forest Model Training
↓
Model Evaluation
↓
Model Saving
↓
Dashboard Integration
↓
Soil Fertility Prediction
↓
Crop Recommendation

## Project Files

| File | Description |
|---|---|
| `minor_project.ipynb` | Google Colab notebook containing model development |
| `soil_model.pkl` | Trained machine learning model |
| `app.py` | Application/dashboard code |
| `requirements.txt` | Required Python libraries |

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt


## Future Enhancements
Integration of additional soil parameters
More detailed soil-type classification
Support for more crop categories
Larger and more diverse datasets
Improved model performance through hyperparameter tuning
Cloud-based deployment for continuous access
