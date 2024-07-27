# app/pages/main.py

import streamlit as st
from app.utils.helper_functions import get_unique_symptoms, predict_disease
import pandas as pd
from app.components.header import render_header

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
                ('bot', 'I can help identify potential diseases based on the symptoms you provide.'),
                ('bot', 'Please enter your symptom:')
            ]
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False
        if 'prediction_made' not in st.session_state:
            st.session_state.prediction_made = False

        # Function to add a new symptom input box with autocomplete
        def add_symptom_input():
            selected_symptom = st.selectbox(
                'Please choose your symptom here:',
                [''] + unique_symptoms.tolist(),
                key=f'symptom_input_{len(st.session_state.symptoms)}'
            )
            if selected_symptom and selected_symptom not in st.session_state.symptoms:
                st.session_state.symptoms.append(selected_symptom)
                st.session_state.conversation.append(('user', selected_symptom))
                
                # Update bot message based on the number of symptoms
                if len(st.session_state.symptoms) == 1:
                    st.session_state.conversation.append(('bot', 'Please enter your next symptom:'))
                elif len(st.session_state.symptoms) < 10:
                    st.session_state.conversation.append(('bot', 'Enter any extra symptoms you have, or press \'Submit\' to get your diagnosis.'))
                else:
                    st.session_state.conversation.append(('bot', 'Enter any extra symptoms you have, or press \'Submit\' to get your diagnosis.'))
                
                st.experimental_rerun()

        # Display conversation
        conversation = st.session_state.conversation
        for i, (speaker, message) in enumerate(conversation):
            if speaker == 'bot':
                st.markdown(f"<div class='bot-message'>{message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)

        # Add symptom input box if the limit of 10 symptoms has not been reached and not submitted
        if len(st.session_state.symptoms) < 10 and not st.session_state.submitted:
            add_symptom_input()

        # Show submit button if there are at least two symptoms and prediction has not been made
        if len(st.session_state.symptoms) >= 2 and not st.session_state.prediction_made:
            if st.button('Submit', key='submit_button', help='Submit your symptoms to get a prediction'):
                st.session_state.submitted = True
                if st.session_state.symptoms:
                    prediction = predict_disease(st.session_state.symptoms)
                    st.session_state.conversation.append(('bot', f'You might have: {prediction}'))
                    st.session_state.prediction_made = True
                    st.experimental_rerun()
                else:
                    st.write('Please enter and select symptoms to predict.')

        # Add reset button to allow users to start over
        if st.session_state.prediction_made:
            if st.button('Reset', key='reset_button', help='Reset to enter new symptoms'):
                st.session_state.symptoms = []
                st.session_state.conversation = [
                    ('bot', 'I can help identify potential diseases based on the symptoms you provide.'),
                    ('bot', 'Please enter your symptom:')
                ]
                st.session_state.submitted = False
                st.session_state.prediction_made = False
                st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
