
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("churn_model.joblib")

# Page configuration
st.set_page_config(
    page_title="Telecom Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# Application title
st.title("📊 Telecom Customer Churn Predictor")
st.write(
    "Enter customer information below to predict "
    "whether the customer is likely to leave the telecom company."
)

st.divider()

# Customer information form
st.header("Customer Information")

with st.form("customer_form"):

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Has Partner?", ["Yes", "No"])
        dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
        tenure = st.number_input("Tenure (Months)", 0, 72, 12)

        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes", "No phone service"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        online_security = st.selectbox(
            "Online Security",
            ["Yes", "No", "No internet service"]
        )

    with col2:
        online_backup = st.selectbox(
            "Online Backup",
            ["Yes", "No", "No internet service"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["Yes", "No", "No internet service"]
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["Yes", "No", "No internet service"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No", "No internet service"]
        )

        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0,
        value=70.0,
        step=1.0
    )

    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        value=840.0,
        step=1.0
    )

    submitted = st.form_submit_button(
        "Predict Customer Churn",
        use_container_width=True
    )

# Prediction
if submitted:

    customer_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    prediction = model.predict(customer_data)[0]

    # Get probability for the churn class
    churn_index = list(model.classes_).index("Yes")
    churn_probability = model.predict_proba(customer_data)[0][churn_index]

    st.divider()
    st.header("Prediction Result")

    st.metric(
        "Estimated Churn Probability",
        f"{churn_probability * 100:.2f}%"
    )

    st.progress(float(churn_probability))

    if prediction == "Yes":
        st.error("⚠️ This customer is predicted to CHURN.")

        if churn_probability >= 0.70:
            st.subheader("Risk Level: High")
        elif churn_probability >= 0.40:
            st.subheader("Risk Level: Medium")
        else:
            st.subheader("Risk Level: Low")

        st.info(
            "Recommendation: Contact this customer, review their "
            "pricing plan, and consider personalized retention offers."
        )

    else:
        st.success("✅ This customer is predicted to STAY.")

        st.info(
            "Recommendation: Continue providing good service and "
            "maintain customer engagement."
        )
