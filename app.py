import streamlit as st
import pandas as pd
import joblib
import os

# Page config
st.set_page_config(
    page_title="ChurnGuard AI",
    page_icon="🔮",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    model = joblib.load("model/churn_model_rf.pkl")
    features = joblib.load("model/model_columns.pkl")
    return model, features

model, feature_names = load_model()

# Header
st.title("🔮 ChurnGuard AI")
st.markdown("### Customer Churn Prediction")
st.markdown("Developed by **M Fayaz Khan**")
st.markdown("---")

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["👤 Personal", "📱 Services", "🛡️ Security", "📺 Streaming", "💰 Billing"]
)

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    with col2:
        partner = st.selectbox("Partner", ["No", "Yes"])
        dependents = st.selectbox("Dependents", ["No", "Yes"])
    with col3:
        tenure = st.number_input("Tenure (months)", 0, 72, 12)

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        phone = st.selectbox("Phone Service", ["Yes", "No"])
    with col2:
        multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    with col3:
        internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
        backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    with col2:
        protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
        support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    with col2:
        movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

with tab5:
    col1, col2, col3 = st.columns(3)
    with col1:
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    with col2:
        payment = st.selectbox("Payment Method", 
            ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    with col3:
        monthly = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
        total = st.number_input("Total Charges ($)", 0.0, 10000.0, 500.0)

# Predict button
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict = st.button("🔮 Predict Churn", use_container_width=True)

if predict:
    # Convert inputs to model format
    input_dict = {
        'gender': 1 if gender == "Male" else 0,
        'SeniorCitizen': 1 if senior == "Yes" else 0,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone == "Yes" else 0,
        'PaperlessBilling': 1 if paperless == "Yes" else 0,
        'MonthlyCharges': monthly,
        'TotalCharges': total,
        'MultipleLines_No phone service': 1 if multiple == "No phone service" else 0,
        'MultipleLines_Yes': 1 if multiple == "Yes" else 0,
        'InternetService_Fiber optic': 1 if internet == "Fiber optic" else 0,
        'InternetService_No': 1 if internet == "No" else 0,
        'OnlineSecurity_No internet service': 1 if security == "No internet service" else 0,
        'OnlineSecurity_Yes': 1 if security == "Yes" else 0,
        'OnlineBackup_No internet service': 1 if backup == "No internet service" else 0,
        'OnlineBackup_Yes': 1 if backup == "Yes" else 0,
        'DeviceProtection_No internet service': 1 if protection == "No internet service" else 0,
        'DeviceProtection_Yes': 1 if protection == "Yes" else 0,
        'TechSupport_No internet service': 1 if support == "No internet service" else 0,
        'TechSupport_Yes': 1 if support == "Yes" else 0,
        'StreamingTV_No internet service': 1 if tv == "No internet service" else 0,
        'StreamingTV_Yes': 1 if tv == "Yes" else 0,
        'StreamingMovies_No internet service': 1 if movies == "No internet service" else 0,
        'StreamingMovies_Yes': 1 if movies == "Yes" else 0,
        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'PaymentMethod_Credit card (automatic)': 1 if payment == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if payment == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if payment == "Mailed check" else 0
    }
    
    input_df = pd.DataFrame([input_dict])
    input_df = input_df[feature_names]
    
    prob = model.predict_proba(input_df)[0][1]
    pred = "HIGH CHURN RISK" if prob > 0.5 else "LOW CHURN RISK"
    
    # Show results
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if "HIGH" in pred:
            st.error(f"### ⚠️ {pred}")
        else:
            st.success(f"### ✅ {pred}")
    
    with col2:
        st.metric("Churn Probability", f"{prob:.1%}")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Probability", f"{prob:.1%}")
    col2.metric("Tenure", f"{tenure} months")
    col3.metric("Monthly", f"${monthly:.2f}")
    col4.metric("Total", f"${total:.0f}")
    
    # Recommendations
    st.markdown("---")
    if "HIGH" in pred:
        st.warning("""
        ### 📋 Business Recommendations
        - Send 25% retention discount for next 3 months
        - Schedule priority customer success call
        - Offer free upgrade to annual contract
        - Add to high-risk monitoring list
        """)
    else:
        st.info("""
        ### 📋 Business Recommendations
        - Send satisfaction survey with 10% discount
        - Offer referral program - Get $50 credit
        - Consider upsell opportunities
        - Regular engagement campaign
        """)
