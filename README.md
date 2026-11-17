
# Customer Churn Prediction - PSEB

A Machine Learning project that predicts whether a telecom customer is likely to leave the company using customer data and classification algorithms.

## 🚀 Live Application

[Telecom Customer Churn Predictor](https://customer-churn-project-pseb.streamlit.app/)

## 📊 Project Overview

- Dataset: Telco Customer Churn
- Total Records: 7,043
- Target Variable: `Churn`
- Problem Type: Binary Classification
- Train-Test Split: 80/20

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest

**Selected Model:** Logistic Regression

GridSearchCV with 5-fold cross-validation was used for hyperparameter tuning.

## 🏆 Final Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 73.81% |
| Precision | 50.43% |
| Recall | 78.34% |
| F1-Score | 61.36% |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- Google Colab

## 📁 Project Structure

```text
customer-churn-project-pseb/
│
├── app.py
├── churn_model.joblib
├── requirements.txt
└── README.md
```

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 Objective

To identify customers who are likely to churn and help telecom businesses improve customer retention through data-driven decisions.

---

**Developed as part of the PSEB AI Bootcamp.**
