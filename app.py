import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ------------------------------
# 🌐 Page Configuration
# ------------------------------
st.set_page_config(
    page_title="🏦 Loan Approval Predictor",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------
# 🖼️ Header Image from Web
# ------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <img src="https://img.freepik.com/premium-photo/loan-approval-business-finance-concept-hand-holding-pen-pointing-text-loan-approval_1028938-112752.jpg" 
        alt="Loan Approval Banner" width="700"/>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# 🎯 App Title & Description
# ------------------------------
st.title("🏦 Loan Approval Prediction App")
st.markdown("""
### Predict Loan Approval using Machine Learning  
This app helps financial institutions and users estimate **loan approval chances** based on applicant information.
""")

# ------------------------------
# 🧾 Sidebar – Contact Info
# ------------------------------
st.sidebar.header("👤 Developer Info")
st.sidebar.markdown("""
**Developed by:** Pranav Gaikwad  
📞 **Contact:** [7028719844](tel:7028719844)  
📧 **Email:** [gaikwadpranav988@gmail.com](mailto:gaikwadpranav988@gmail.com)  
🔗 **GitHub:** [Loan Approval Predictor](https://github.com/pranavgaikwad51/Loan_Approval_Predictor)
""")

st.sidebar.markdown("---")
st.sidebar.info("💡 *AI-powered Financial Prediction Tool*")

# ------------------------------
# 📦 Load the Trained Model
# ------------------------------
with open("Best_model(1).pkl", "rb") as file:
    model = pickle.load(file)

# ------------------------------
# 📋 User Input Section
# ------------------------------
st.header("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ("Male", "Female"))
    married = st.selectbox("Marital Status", ("No", "Yes"))
    dependents = st.selectbox("Number of Dependents", ("0", "1", "2", "3+"))
    education = st.selectbox("Education Level", ("Graduate", "Not Graduate"))
    self_employed = st.selectbox("Self Employed", ("No", "Yes"))

with col2:
    applicant_income = st.number_input("Applicant Income ($)", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income ($)", min_value=0)
    loan_amount = st.number_input("Loan Amount ($)", min_value=0)
    loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0)
    credit_history = st.selectbox("Credit History", ("1.0 - Good", "0.0 - Poor"))
    property_area = st.selectbox("Property Area", ("Urban", "Rural", "Semiurban"))

# ------------------------------
# 🧠 Predict Button
# ------------------------------
if st.button("🔍 Predict Loan Approval"):
    try:
        input_data = np.array([
            1 if gender == "Male" else 0,
            1 if married == "Yes" else 0,
            int(dependents[0]) if dependents != "3+" else 3,
            1 if education == "Graduate" else 0,
            1 if self_employed == "Yes" else 0,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_amount_term,
            1.0 if "Good" in credit_history else 0.0,
            0 if property_area == "Rural" else (1 if property_area == "Semiurban" else 2)
        ]).reshape(1, -1)

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.success("✅ Loan Approved! Congratulations 🎉")
            st.balloons()
        else:
            st.error("❌ Loan Rejected. Please review applicant details.")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ------------------------------
# 📊 Footer Section
# ------------------------------
st.markdown("""
---
💡 **Disclaimer:** This app is for educational and demonstration purposes only.  
Developed by **Pranav Gaikwad** | [GitHub Repository](https://github.com/pranavgaikwad51/Loan_Approval_Predictor)
""")
