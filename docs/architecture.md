# SympCheck Architecture Document

## Table of Contents

1. [Overview](#1-overview)
   - 1.1 [Purpose](#11-purpose)
   - 1.2 [Scope](#12-scope)
2. [Design Principles](#2-design-principles)
3. [System Overview](#3-system-overview)
   - 3.1 [System Components](#31-system-components)
      - 3.1.1 [User Interface (UI)](#311-user-interface-ui)
      - 3.1.2 [Backend Service](#312-backend-service)
      - 3.1.3 [Continuous Integration/Continuous Deployment (CI/CD)](#313-continuous-integrationcontinuous-deployment-cicd)
      - 3.1.4 [Model](#314-model)
   - 3.2 [Architecture Flow](#32-architecture-flow)
4. [User Interaction Flow](#4-user-interaction-flow)
5. [Conclusion](#5-conclusion)




## 1. Overview

SympCheck is an intelligent chatbot designed to diagnose diseases based on user-provided symptoms. The project integrates natural language processing (NLP) techniques with a machine learning model deployed via a Flask API, with a user interface built using Streamlit.

### 1.1. Purpose

This document explains the functionality of SympCheck and serves as a guide for understanding the code and architecture.

### 1.2. Scope

The scope of this document includes the architectural components of the system, their responsibilities, and how they interact to achieve the desired functionality.

## 2. Design Principles

- **User-Centric Design**: Provides an intuitive and interactive interface for seamless user interaction.
- **Scalable Architecture**: Modular design ensures easy maintenance and future expansion.
- **Efficient Processing**: Leverages NLP for quick and accurate disease predictions.
- **Responsive Feedback**: Delivers predictions to enhance user experience.
- **Robust Session Management**: Maintains state to ensure consistent interactions.

## 3. System Overview

### 3.1. System Components

#### 3.1.1. User Interface (UI)

- **SympCheck Chatbot UI**: The user interacts with the system through the SympCheck chatbot UI, which is hosted on Streamlit. The chatbot allows users to input their symptoms in a conversational format.
- **Deployment**: The chatbot UI is deployed on Streamlit, ensuring an accessible and user-friendly interface.

#### 3.1.2. Backend Service

- **Flask API**: The backend is built using Flask, a lightweight web framework. The Flask API is responsible for handling the input from the chatbot UI, processing the symptoms, and returning the predicted disease.
- **Logistic Regression Model**: The Flask API integrates a trained Logistic Regression model to perform the disease prediction based on the symptoms provided by the user.
- **Deployment**: The Flask API, along with the Logistic Regression model, is hosted on Heroku. This ensures scalability and reliability for handling prediction requests from the chatbot UI.

#### 3.1.3. Continuous Integration/Continuous Deployment (CI/CD)

- **GitHub**: Both the SympCheck chatbot UI and the Flask API backend are version-controlled using GitHub. This allows for streamlined collaboration and version management.
- **CI/CD Pipeline**: A continuous integration/continuous deployment pipeline is set up for both the frontend (SympCheck) and the backend (Sympcheckbe). This pipeline ensures that any changes pushed to the GitHub repositories are automatically tested and deployed to their respective platforms (Streamlit for the UI and Heroku for the backend).

#### 3.1.4. Model

- **Data Preparation**: Manages data acquisition, preprocessing, and feature extraction.
- **Model Training and Selection**: Involves the training and validation of machine learning models.
- **Deployment**: The Logistic Regression model is hosted on Heroku along with the Flask API. 

### 3.2. Architecture Flow

![SympCheck Architecture](<Sympcheck (1).jpeg>)

The system loosely follows the MVC pattern, with the Streamlit app serving as the View, the Flask API as the Controller, and the NLP model/data as the Model.

## 4. User Interaction Flow

1. **User Input:** Users enter symptoms in the Streamlit app.
2. **API Request:** The frontend sends a POST request to the `/predict` endpoint of the Flask API with the symptoms.
3. **NLP Model Processing:** The Flask API forwards the symptoms to the NLP model, which predicts the disease.
4. **API Response:** The Flask API returns the predicted disease to the frontend.
5. **Display Results:** The frontend displays the results to the user.


## 5. Conclusion

This document provides a comprehensive overview of the system architecture for the SympCheck application. It outlines the components, data flow, and architectural patterns that together ensure the system's robustness and scalability.