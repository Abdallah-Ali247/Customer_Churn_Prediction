
# 📊 Telco Customer Churn Prediction (Flask Web App)

## 🚀 Overview
This project is a **machine learning–powered web application** built with **Flask** that predicts **customer churn** for a telecom company.  

Users can input customer details (e.g., tenure, charges, services, contract type), and the app will return:
- ✅ Whether the customer is likely to churn (Yes/No)  
- 📈 The probability of churn  

This is an **end-to-end project**: data preprocessing, model training, saving the model, and deploying it as a Flask app with a clean web UI.

---

## 🖼️ Demo UI
The app provides a **modern Bootstrap-styled interface** with radio buttons and input fields for user-friendly data entry:

![UI Screenshot Placeholder](https://via.placeholder.com/800x400.png?text=Telco+Churn+App+Demo)

---

## 🏗️ Project Structure
 
Project/
│── app.py # Flask backend
│── model/ # Saved trained model (XGBoost JSON)
│── templates/
│ └── index.html # UI template
│── static/ # (optional for CSS/JS if needed later)
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── .gitignore # Ignore unnecessary files


---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone  https://github.com/Abdallah-Ali247/Customer_Churn_Prediction.git  
cd Telco-Customer-Churn-Flask
```

### How to use it 
1. Create Virtual Environment
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows

2. Install Dependencies
pip install -r requirements.txt

3. Run the Flask App
python app.py

App will run on:
👉 http://127.0.0.1:5000/



📋 Input Features

The app expects the following customer details:

Tenure (months)

MonthlyCharges

TotalCharges

Contract (Month-to-month / One year / Two year)

InternetService (DSL / Fiber optic / No)

PhoneService (Yes / No)

StreamingTV (Yes / No / No internet service)

StreamingMovies (Yes / No / No internet service)

Gender (Male / Female)

SeniorCitizen (Yes / No)

Partner (Yes / No)

Dependents (Yes / No)

PaperlessBilling (Yes / No)

PaymentMethod (Credit card / Electronic check / Mailed check / Bank transfer)

🤖 Model

Algorithm: XGBoost (Gradient Boosted Trees)

Task: Binary Classification (Churn = Yes/No)

Output:

Prediction: Yes / No

Probability: Value between 0 and 1

### Example Prediction
Tenure = 12
MonthlyCharges = 75.5
TotalCharges = 820.0
Contract = Month-to-month
InternetService = Fiber optic
PhoneService = Yes
StreamingTV = Yes
StreamingMovies = No
Gender = Female
SeniorCitizen = No
Partner = No
Dependents = No
PaperlessBilling = Yes
PaymentMethod = Electronic check

👨‍💻 Author

Abdallah Ali

💼 Full Stack Developer & AI Engineer


reformat it in readme file format
