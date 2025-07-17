
# 📉 Customer Churn Prediction

This project predicts customer churn using a machine learning pipeline trained on telco data. The model uses LightGBM, Optuna hyperparameter tuning, and SHAP explainability. A Streamlit app is provided for interactive prediction.

## 📂 Files Included

| File Name                          | Description |
|-----------------------------------|-------------|
| `customer_churn_prediction.ipynb` | Jupyter notebook with full EDA, preprocessing, modeling, and SHAP |
| `final_model_pipeline.pkl`        | Trained model pipeline including preprocessing |
| `best_threshold.txt`              | Optimal threshold (TPR - FPR maximized) |
| `top_20_features.json`            | Top 20 features based on SHAP importance |
| `requirements.txt`                | Python dependencies for Streamlit Cloud |
| `churn_app.py`                    | Streamlit app code |

## 🚀 Try It Live

🔗 [Launch the App](https://customerchurn-prediction-jerryab31.streamlit.app)

> Predict customer churn using a LightGBM model trained on telco data. Includes SHAP explainability and threshold tuning.

## 🗃️ Dataset

**Telco Customer Churn Dataset** (available at: [Kaggle Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn))

## 💡 Features Used

Top 20 features (based on SHAP importance) are used in the model. These include `Contract`, `tenure`, `MonthlyCharges`, `OnlineSecurity`, `InternetService`, and more.

## 📦 Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit app locally

```bash
streamlit run churn_app.py
```

## ☁️ Deploy on Streamlit Cloud

Upload the following files to your Streamlit Cloud repo:

- `churn_app.py`
- `final_model_pipeline.pkl`
- `best_threshold.txt`
- `top_20_features.json`
- `requirements.txt`

The app will auto-deploy. Add the URL in the README.

## 📌 Coming Soon

- 📊 Enhanced dashboard UI
- 🧠 Auto retraining pipeline
- 🔗 Database integration for real-time inputs

---

Made with ❤️ by Jerry Abraham
