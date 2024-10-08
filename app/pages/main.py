# app/pages/main.py

#import required libraries and functions
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.helper_functions import get_unique_symptoms, predict_disease
import pandas as pd
from components.header import render_header
from utils.messages import BOT_MESSAGES

# Load the dataset from CSV
df = pd.read_csv('public/assets/queries.csv')

# Streamlit UI components
def main():
    st.set_page_config(page_title='SympCheck', page_icon=':hospital:', layout='wide')

    # Include CSS styles
    with open('app/styles/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Include HTML header
    render_header()

    # Add a container for the content with space for the fixed header
    with st.container():
        st.markdown('<div class="content">', unsafe_allow_html=True)
        # Get unique symptoms
        unique_symptoms = get_unique_symptoms(df)

        # Initialize session state for symptoms and conversation
        if 'symptoms' not in st.session_state:
            st.session_state.symptoms = []
        if 'conversation' not in st.session_state:
            st.session_state.conversation = [
                ('bot', BOT_MESSAGES["welcome"]),
                ('bot', BOT_MESSAGES["ask_symptom"])
            ]
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False
        if 'prediction_made' not in st.session_state:
            st.session_state.prediction_made = False

        # Function to add a new symptom input box with autocomplete
        def add_symptom_input():
            available_symptoms = unique_symptoms.tolist()

            # Remove symptoms that have already been selected
            available_symptoms = [symptom for symptom in available_symptoms if symptom not in st.session_state.symptoms]

            selected_symptom = st.selectbox(
                'Please choose your symptom here:',
                [''] + available_symptoms,
                key=f'symptom_input_{len(st.session_state.symptoms)}'
            )
            if selected_symptom:
                if selected_symptom not in st.session_state.symptoms:
                    st.session_state.symptoms.append(selected_symptom)
                    st.session_state.conversation.append(('user', selected_symptom))
                    
                    # Update bot message based on the number of symptoms
                    if len(st.session_state.symptoms) == 1:
                        st.session_state.conversation.append(('bot', BOT_MESSAGES["next_symptom"]))
                    elif len(st.session_state.symptoms) < 10:
                        st.session_state.conversation.append(('bot', BOT_MESSAGES["extra_symptoms"]))
                    else:
                        st.session_state.conversation.append(('bot', BOT_MESSAGES["max_symptoms"]))

                    st.rerun()

                else:
                    st.session_state.conversation.append(('bot', BOT_MESSAGES["already_selected"]))
        
        # Display conversation
        conversation = st.session_state.conversation
        for i, (speaker, message) in enumerate(conversation):
            if speaker == 'bot':
                st.markdown(f"<div class='bot-message'>{message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)

        # Show symptom input box
        if len(st.session_state.symptoms) < 10 and not st.session_state.submitted:
            add_symptom_input()

        # Show submit button if there are at least two symptoms and prediction has not been made
        if len(st.session_state.symptoms) >= 2 and not st.session_state.prediction_made:
            if st.button('Submit', key='submit_button', help='Submit your symptoms to get a prediction'):
                st.session_state.submitted = True
                if st.session_state.symptoms:
                    prediction = predict_disease(st.session_state.symptoms)
                    st.session_state.conversation.append(('bot', BOT_MESSAGES["prediction_result"].format(prediction)))
                    st.session_state.prediction_made = True
                    st.rerun()
                else:
                    st.write('Please enter and select symptoms to predict.')

        # Add reset button to allow users to start over
        if st.session_state.prediction_made:
            if st.button('Reset', key='reset_button', help='Reset to enter new symptoms'):
                st.session_state.symptoms = []
                st.session_state.conversation = [
                    ('bot', BOT_MESSAGES["reset_intro"]),
                    ('bot', BOT_MESSAGES["ask_symptom"])
                ]
                st.session_state.submitted = False
                st.session_state.prediction_made = False
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

