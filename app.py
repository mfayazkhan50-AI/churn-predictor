from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model
model_path = os.path.join("model", "churn_model_rf.pkl")
columns_path = os.path.join("model", "model_columns.pkl")

model = joblib.load(model_path)
feature_names = joblib.load(columns_path)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    gender: str = Form("Male"),
    senior_citizen: str = Form("No"),
    partner: str = Form("No"),
    dependents: str = Form("No"),
    tenure: int = Form(12),
    phone_service: str = Form("Yes"),
    multiple_lines: str = Form("No"),
    internet_service: str = Form("DSL"),
    online_security: str = Form("No"),
    online_backup: str = Form("No"),
    device_protection: str = Form("No"),
    tech_support: str = Form("No"),
    streaming_tv: str = Form("No"),
    streaming_movies: str = Form("No"),
    contract: str = Form("Month-to-month"),
    paperless_billing: str = Form("Yes"),
    payment_method: str = Form("Electronic check"),
    monthly_charges: float = Form(70.0),
    total_charges: float = Form(500.0)
):
    # Convert to model format
    input_dict = {
        'gender': 1 if gender == "Male" else 0,
        'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone_service == "Yes" else 0,
        'PaperlessBilling': 1 if paperless_billing == "Yes" else 0,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'MultipleLines_No phone service': 1 if multiple_lines == "No phone service" else 0,
        'MultipleLines_Yes': 1 if multiple_lines == "Yes" else 0,
        'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
        'InternetService_No': 1 if internet_service == "No" else 0,
        'OnlineSecurity_No internet service': 1 if online_security == "No internet service" else 0,
        'OnlineSecurity_Yes': 1 if online_security == "Yes" else 0,
        'OnlineBackup_No internet service': 1 if online_backup == "No internet service" else 0,
        'OnlineBackup_Yes': 1 if online_backup == "Yes" else 0,
        'DeviceProtection_No internet service': 1 if device_protection == "No internet service" else 0,
        'DeviceProtection_Yes': 1 if device_protection == "Yes" else 0,
        'TechSupport_No internet service': 1 if tech_support == "No internet service" else 0,
        'TechSupport_Yes': 1 if tech_support == "Yes" else 0,
        'StreamingTV_No internet service': 1 if streaming_tv == "No internet service" else 0,
        'StreamingTV_Yes': 1 if streaming_tv == "Yes" else 0,
        'StreamingMovies_No internet service': 1 if streaming_movies == "No internet service" else 0,
        'StreamingMovies_Yes': 1 if streaming_movies == "Yes" else 0,
        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'PaymentMethod_Credit card (automatic)': 1 if payment_method == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if payment_method == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if payment_method == "Mailed check" else 0
    }
    
    input_df = pd.DataFrame([input_dict])
    input_df = input_df[feature_names]
    
    prob = model.predict_proba(input_df)[0][1]
    pred = "HIGH CHURN RISK" if prob > 0.5 else "LOW CHURN RISK"
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": pred,
        "probability": f"{prob:.1%}",
        "prob_raw": prob,
        "gender": gender,
        "senior_citizen": senior_citizen,
        "partner": partner,
        "dependents": dependents,
        "tenure": tenure,
        "phone_service": phone_service,
        "multiple_lines": multiple_lines,
        "internet_service": internet_service,
        "online_security": online_security,
        "online_backup": online_backup,
        "device_protection": device_protection,
        "tech_support": tech_support,
        "streaming_tv": streaming_tv,
        "streaming_movies": streaming_movies,
        "contract": contract,
        "paperless_billing": paperless_billing,
        "payment_method": payment_method,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges
    })