# app/components/header.py

import streamlit as st

def render_header():
    st.markdown("""
        <style>
            .header {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                text-align: center;
                background-color: white;
                z-index: 1000; /* Ensure header is above other content */
                padding: 40px 0; /* Increased top padding to ensure full visibility */
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .sympcheck {
                font-size: 48px;
                color: #0066ff;
                font-weight: bold;
                margin: 0;
            }
            .stethoscope {
                font-size: 40px; /* Adjust size to match the font size of 'SympCheck' */
                color: #0066ff;
                margin-right: 0; /* Remove any margin to make it right next to the text */
                padding-right: 0; /* Remove any padding */
            }
            .your-health-mate {
                font-size: 14px;
                color: black;
                margin-top: 10px; /* Adjust margin to reduce space between header and tagline */
            }
            .emoji {
                font-size: 20px;
                margin-left: 5px;
            }
            .content {
                margin-top: calc(40px + 2rem); /* Adjust this value to control space between header and content */
            }
            .bot-message, .user-message {
                border-radius: 20px;
                padding: 10px;
                margin-bottom: 5px; /* Adjusted margin-bottom */
                display: inline-block;
                max-width: 70%;
                position: relative;
                line-height: 1.5; /* Increased line-height for better readability */
            }
            .bot-message {
                background-color: #d6eaff;
                color: black;
                text-align: left;
                float: left;
                margin-right: 20px;
                margin-top: 20px;
            }
            .bot-message:after {
                content: '';
                position: absolute;
                top: 50%;
                left: -10px;
                width: 0;
                height: 0;
                border: 10px solid transparent;
                border-right-color: #d6eaff;
                border-left: 0;
                border-bottom: 0;
                margin-top: -5px;
            }
            .user-message {
                background-color: #d4edda;
                color: black;
                text-align: left;
                float: right;
                margin-left: 20px;
                margin-top: 20px;
            }
            .user-message:after {
                content: '';
                position: absolute;
                top: 50%;
                right: -10px;
                width: 0;
                height: 0;
                border: 10px solid transparent;
                border-left-color: #d4edda;
                border-right: 0;
                border-bottom: 0;
                margin-top: -5px;
            }
        </style>
        <div class="header">
            <div class="stethoscope">🩺</div>
            <div class="sympcheck">SympCheck</div>
            <div class="your-health-mate">your health mate</div>
        </div>
    """, unsafe_allow_html=True)
