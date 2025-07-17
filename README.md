# 📊 Customer Churn Prediction using Machine Learning

![Status](https://img.shields.io/badge/Streamlit-App--Coming--Soon-orange?logo=streamlit)
![License](https://img.shields.io/badge/Machine%20Learning-LightGBM-blue?style=flat&logo=github)

An explainable machine learning project that predicts customer churn for a telecom provider. Designed with business stakeholders in mind, it balances **accuracy, interpretability, and usability**.

---

## 🗂️ Project Contents

| File                             | Description |
|----------------------------------|-------------|
| `churn_app.py`                   | Streamlit app for user input and prediction |
| `final_model_pipeline.pkl`       | Trained model pipeline (LightGBM + preprocessing) |
| `best_threshold.txt`             | Custom threshold (0.33) for decision cutoff |
| `top_20_features.json`           | Top 20 SHAP-ranked features |
| `customer_churn_prediction.ipynb`| Full notebook: training, SHAP, thresholding |
| `requirements.txt`               | Dependencies for the project |

---

## 📥 Data Source

The dataset used in this project is a **public telecom churn dataset**, available from:

🔗 [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

It contains customer attributes like:
- Demographics
- Subscription details
- Service usage
- Monthly charges and tenure
- Whether the customer churned

---

## 🚀 Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction

pip install -r requirements.txt

streamlit run churn_app.py


🧠 Model Highlights
⚡ LightGBM Classifier trained with Optuna-tuned hyperparameters

✅ Preprocessing pipeline using ColumnTransformer

🔍 Feature importance from SHAP values

🎯 Adjusted classification threshold (0.33) to improve recall for churners

🏆 Only top 20 SHAP features used in final app

🎛️ Streamlit App
The app will allow users to:

Enter new customer details

Get a churn probability

Show Likely to Stay or Likely to Churn

🔗 Live App URL
Coming Soon – Will be deployed on Streamlit Cloud

✨ Example Features Used
Contract

MonthlyCharges

tenure

InternetService, OnlineSecurity, TechSupport

Full list: see top_20_features.json

👤 Author
Jerry Abraham
Certified Lean Six Sigma Black Belt
Machine Learning | Explainable AI | BFSI & Telecom Use Cases

📄 License
This project is for educational purposes. Feel free to fork or adapt it for learning and demonstration.
