# Loan Approval Prediction Project

## 📌 Project Overview
This project is a **machine learning solution** designed to predict whether a loan application will be approved based on applicant features such as income, credit score, loan amount, years employed, and points. The system uses multiple classification algorithms to ensure accurate predictions, helping financial institutions make data-driven lending decisions.

---

## 🧰 Technologies Used
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Pickle  
- **Algorithms Implemented:**  
  - K-Nearest Neighbors (KNN)  
  - Naive Bayes (NB)  
  - Logistic Regression (LR)  
  - Support Vector Machine (SVM)

---

## 📊 Dataset
- **Source:** `loan_approval.csv`  
- **Number of Entries:** 2,000  
- **Columns:**
  - `income` – Applicant income  
  - `credit_score` – Creditworthiness score  
  - `loan_amount` – Requested loan amount  
  - `years_employed` – Years of employment  
  - `points` – Applicant points  
  - `loan_approved` – Target variable (True/False)  

---

## ⚙️ Model Training
- The dataset was split **80% for training** and **20% for testing**.  
- Four models were trained to predict loan approval: KNN, Naive Bayes, Logistic Regression, and SVM.

---

## 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|---------|----------|-------|----------|
| KNN | 61% | 0.60 | 0.59 | 0.59 |
| Naive Bayes | 95% | 0.95 | 0.95 | 0.95 |
| Logistic Regression | 83% | 0.83 | 0.83 | 0.83 |
| SVM | 65% | 0.67 | 0.63 | 0.61 |

**Insight:**  
- **Naive Bayes** achieved the highest accur
