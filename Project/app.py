from flask import Flask, request, render_template
import joblib
import pandas as pd
import xgboost as xgb



app = Flask(__name__)

# Load model and training columns
# model = joblib.load(r"model\xgb_churn_model.pkl")
model = xgb.Booster()
model.load_model(r"model\xgb_model.json")

# columns
training_columns = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
       'avg_monthly_spend', 'services_count', 'gender_Male', 'Partner_Yes',
       'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service',
       'MultipleLines_Yes', 'InternetService_Fiber optic',
       'InternetService_No', 'OnlineSecurity_No internet service',
       'OnlineSecurity_Yes', 'OnlineBackup_No internet service',
       'OnlineBackup_Yes', 'DeviceProtection_No internet service',
       'DeviceProtection_Yes', 'TechSupport_No internet service',
       'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes',
       'StreamingMovies_No internet service', 'StreamingMovies_Yes',
       'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
       'tenure_group_13-24', 'tenure_group_25+', 'tenure_group_nan']

def preprocess_input(df):
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, 72],
        labels=['0-12','12-24','24-48','48-60','60-72'],
        right=False
    ).astype(str)

    df['AvgMonthlySpend'] = df['TotalCharges'] / df['tenure'].replace(0, 1)

    service_cols = ['PhoneService','InternetService','StreamingTV','StreamingMovies']
    df['ServiceCount'] = df[service_cols].apply(lambda x: sum(x=='Yes'), axis=1)

    df = pd.get_dummies(df, drop_first=False)
    df = df.reindex(columns=training_columns, fill_value=0)

    return df

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    prob = None

    if request.method == "POST":
        data = {
            "tenure": int(request.form["tenure"]),
            "MonthlyCharges": float(request.form["MonthlyCharges"]),
            "TotalCharges": float(request.form["TotalCharges"]),
            "Contract": request.form["Contract"],
            "InternetService": request.form["InternetService"],
            "PhoneService": request.form["PhoneService"],
            "StreamingTV": request.form["StreamingTV"],
            "StreamingMovies": request.form["StreamingMovies"],
            "gender": request.form["gender"],
            "SeniorCitizen": int(request.form["SeniorCitizen"]),
            "Partner": request.form["Partner"],
            "Dependents": request.form["Dependents"],
            "PaperlessBilling": request.form["PaperlessBilling"],
            "PaymentMethod": request.form["PaymentMethod"],
        }

    #     df = pd.DataFrame([data])
    #     processed = preprocess_input(df)

    #     prob = model.predict_proba(processed)[:, 1][0]
    #     prediction = "Yes" if prob >= 0.5 else "No"
    #     prob = round(float(prob), 4)

    # return render_template("index.html", prediction=prediction, prob=prob)


        df = pd.DataFrame([data])
        processed = preprocess_input(df)

        dtest = xgb.DMatrix(processed)
        prob = model.predict(dtest)[0]
        prediction = "Yes" if prob >= 0.5 else "No"
        prob = round(float(prob), 4)

    return render_template("index.html", prediction=prediction, prob=prob)


if __name__ == "__main__":
    app.run(debug=True)
