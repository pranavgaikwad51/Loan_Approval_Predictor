import streamlit as st
import pickle
import numpy as np
import os

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
# 🖼️ Header Image (Banker Advising Clients)
# ------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <img src="https://img.freepik.com/premium-photo/banker-explaining-loan-options-couple-office-professional-advisor-financial-consultant-discussing-mortgage-application-with-clients-finance-business-meeting-banking_590464-220196.jpg" 
        alt="Banker Advising Loan Clients" width="700"/>
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
Estimate **loan approval probability** based on applicant details and credit history.
""")

# ------------------------------
# 🧾 Sidebar – Developer Info
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
# 📦 Load the Trained Model (Safe Handling)
# ------------------------------
model_path = "Best_model.pkl"

if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
else:
    st.error("❌ Model file not found! Please make sure 'Best_model.pkl' is in the same folder as 'app.py'.")
    st.stop()

# ------------------------------
# 📋 Applicant Information
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
        st.error(f"⚠️ Error during prediction: {e}")

# ------------------------------
# 📊 Footer
# ------------------------------
st.markdown("""
---
💡 **Disclaimer:** This app is for educational purposes only.  
Developed by **Pranav Gaikwad** | [GitHub Repository](https://github.com/pranavgaikwad51/Loan_Approval_Predictor)
""")
