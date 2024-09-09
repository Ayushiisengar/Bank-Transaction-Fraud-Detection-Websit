# Bank Transaction Fraud Detection Web Application
## Overview
This project is a web application designed to predict fraudulent bank transactions using various machine learning models. Built with Flask, the application allows users to authenticate, select a machine learning model, input transaction features, and view prediction results. The application also tracks the history of predictions made during a session.

## Features
**User Authentication**: Secure login functionality to restrict access to authorized users.
**Model Selection**: Users can choose from Logistic Regression, Random Forest, and Support Vector Machine (SVM) models for prediction.
**Transaction Prediction**: Predicts whether a transaction is valid or fraudulent based on user-input features.
**Prediction History**: Tracks and displays a history of predictions made during the session.

## Technologies Used
**Backend**: Flask (Python)
**Frontend**: HTML, CSS, JavaScript
**Machine Learning**: scikit-learn, pandas
**Data Handling**: pandas

## Models Implemented
Logistic Regression
Random Forest Classifier
Support Vector Machine (SVM)

## Installation

Clone the repository:

git clone https://github.com/yourusername/bank-fraud-detection.git

Navigate to the project directory:

cd bank-fraud-detection

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

python app.py

Open a web browser and go to http://127.0.0.1:5000/ to access the application.

## Usage
Login: Use the credentials admin / password to log in.

Model Selection: Choose a machine learning model from the options provided.


Input Features: Enter the transaction features as prompted.

Prediction: View the result indicating whether the transaction is valid or fraudulent.

History: Check the history of all predictions made in the current session.

## Dataset
The application uses a subset of the Credit Card Fraud Detection Dataset from Kaggle. The dataset is balanced by downsampling the majority class (valid transactions) to match the minority class (fraudulent transactions).

## Future Enhancements
Add more models: Implement additional machine learning models for comparison.
Improve UI/UX: Enhance the user interface for better usability.
Model Evaluation: Provide model performance metrics like accuracy, precision, and recall.
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
The dataset used in this project is provided by Kaggle.
The Flask framework was used to develop the web application.
The scikit-learn and pandas libraries were used for machine learning and data handling.
