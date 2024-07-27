# app/utils/helper_functions.py

import requests
from .config import API_URL

def get_unique_symptoms(df):
    return df['query'].unique()

def predict_disease(symptoms):
    try:
        symptoms_str = ', '.join(symptoms)
        response = requests.post(API_URL, json={'symptoms': symptoms_str})
        if response.status_code == 200:
            return response.json()['prediction']
        else:
            return "Prediction failed"
    except Exception as e:
        return str(e)
