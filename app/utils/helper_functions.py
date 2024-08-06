# app/utils/helper_functions.py
import json
import requests

import requests
from .config import API_URL

def get_unique_symptoms(df):
    return df['query'].unique()

def predict_disease(symptoms):
    try:
        # Manually create the JSON string
        symptoms_str = ', '.join(symptoms)
        json_data = json.dumps({"symptoms": symptoms_str})  # Convert dictionary to JSON string
        
        # Send the request
        response = requests.post(API_URL, data=json_data, headers={"Content-Type": "application/json", "Accept": "application/json"})
        # Print the JSON string for debugging
        print("request", json_data)  
        if response.status_code == 200:
            return response.json()['prediction']
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "Prediction failed"
    except Exception as e:
        return str(e)
