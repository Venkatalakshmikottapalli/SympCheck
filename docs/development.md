# SympCheck Design Document

## Table of Contents
1. [Overview](#1-overview)
2. [Design Principles](#2-design-principles)
3. [System Overview](#3-system-overview)
   - 3.1 [System Components](#31-system-components)
   - 3.2 [Architecture Flow](#32-architecture-flow)
4. [Implementation Strategy](#4-implementation-strategy)
   - 4.1 [Technology Stack](#41-technology-stack)
   - 4.2 [Development Workflow](#42-development-workflow)
   - 4.3 [Deployment Process](#43-deployment-process)
   - 4.4 [Project Directory Structure](#44-project-directory-structure)
5. [Testing and Validation](#5-testing-and-validation)
   - 5.1 [Unit Testing](#51-unit-testing)
   - 5.2 [Integration Testing](#52-integration-testing)
   - 5.3 [User Acceptance Testing](#53-user-acceptance-testing)
6. [Security and Privacy Considerations](#6-security-and-privacy-considerations)
   - 6.1 [Data Security](#61-data-security)
   - 6.2 [User Privacy](#62-user-privacy)
7. [Conclusion](#7-conclusion)

## 1. Overview
SympCheck is an intelligent chatbot designed to diagnose diseases based on user-provided symptoms. The project integrates natural language processing (NLP) techniques with a machine learning model deployed via a Flask API, with a user interface built using Streamlit.

## 2. Design Principles
- **User-Centric Design**: Provides an intuitive and interactive interface for seamless user interaction.
- **Scalable Architecture**: Modular design ensures easy maintenance and future expansion.
- **Efficient Processing**: Leverages NLP for quick and accurate disease predictions.
- **Responsive Feedback**: Delivers predictions to enhance user experience.
- **Robust Session Management**: Maintains state to ensure consistent interactions.

## 3. System Overview

### 3.1 System Components

#### 3.1.1 User Interface (UI)
- **SympCheck Chatbot UI**: The user interacts with the system through the SympCheck chatbot UI, which is hosted on Streamlit. The chatbot allows users to input their symptoms in a conversational format.
- **Deployment**: The chatbot UI is deployed on Streamlit, ensuring an accessible and user-friendly interface.

#### 3.1.2 Backend Service
- **Flask API**: The backend is built using Flask. The API processes user input and returns the predicted disease.
- **Logistic Regression Model**: A trained Logistic Regression model is integrated into the Flask API for predictions.
- **Deployment**: The Flask API and model are hosted on Heroku for scalability and reliability.

#### 3.1.3 Continuous Integration/Continuous Deployment (CI/CD)
- **GitHub**: Version control is managed via GitHub.
- **CI/CD Pipeline**: Automated testing and deployment processes are implemented.

#### 3.1.4 Model
- **Data Preparation**: Involves data acquisition, preprocessing, and feature extraction.
- **Model Training and Selection**: Models are trained and validated before deployment.
- **Deployment**: Models are deployed alongside the Flask API.

### 3.2 Architecture Flow
The system loosely follows the MVC pattern, with the Streamlit app serving as the View, the Flask API as the Controller, and the NLP model/data as the Model.

## 4. Implementation Strategy

### 4.1 Technology Stack
- **Frontend**: Streamlit
- **Backend**: Flask
- **Machine Learning**: Scikit-learn, Pandas
- **CI/CD**: GitHub, Heroku

### 4.2 Development Workflow
- **Version Control**: GitHub is used for version control and collaboration.
- **Branching Strategy**: Feature branches are used for development, with pull requests for code reviews.

### 4.3 Deployment Process
- **CI/CD Pipeline**: Automated tests are run on each push to the repository, followed by automatic deployment to Streamlit (UI) and Heroku (backend).

### 4.4 Project Directory Structure
The project follows a structured directory layout to maintain organization and facilitate development:


## 5. Testing and Validation

### 5.1 Unit Testing
Unit tests are written to validate the functionality of individual components.

### 5.2 Integration Testing
Integration tests ensure that different components work together as expected.

### 5.3 User Acceptance Testing
User acceptance tests are conducted to validate the system from the end-user perspective.

## 6. Security and Privacy Considerations

### 6.1 Data Security
- **Encryption**: All data transmitted between the UI and backend is encrypted.
- **Access Control**: API endpoints are protected to prevent unauthorized access.

### 6.2 User Privacy
- **Data Minimization**: Only essential data is collected and processed.
- **Compliance**: The system adheres to data privacy regulations, ensuring user data is handled securely.

## 7. Conclusion
This design document outlines the architecture, implementation strategy, testing, and security considerations for the SympCheck application. The structured approach ensures scalability, maintainability, and security in the system.
