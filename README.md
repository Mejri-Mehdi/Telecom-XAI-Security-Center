<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/SHAP-6E6E6E?style=for-the-badge&logo=shap&logoColor=white" alt="SHAP"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge" alt="Production"/>
</p>






# 🛡️ Enterprise Telecom XAI Security Center

An Explainable Artificial Intelligence (XAI) threat detection pipeline designed to safeguard telecommunications network infrastructure. This system baselines normal operations using an Unsupervised **Isolation Forest** model to detect sophisticated anomalies, then mathematically decodes and translates them into human-readable Threat Intelligence using **SHAP (SHapley Additive exPlanations)**.

---

## 🔗 Live Deployment

The production application is fully deployed and accessible via Streamlit Community Cloud:

👉 **[Launch the Enterprise Telecom XAI Security Center](https://telecom-xai-security-center-h2nvldw84vyk84kcylnvhk.streamlit.app)**

---

## 🚀 Key Features

* **Unsupervised Anomaly Detection:** Leverages an Isolation Forest engine to detect zero-day threats, multi-vector attacks, and infrastructure anomalies without requiring pre-labeled training data.
* **Explainable AI (XAI) Core:** Converts the complex internal decision-making process of the ML model into exact feature-attribution charts via SHAP values, showing analysts *why* a specific log entry was flagged.
* **Production-Grade Data Pipeline:** Built-in multi-stage feature engineering, automated label encoding, and robust data standardization using Scikit-Learn.
* **Interactive Analyst Dashboard:** A scannable visual command center allowing real-time inspection of anomalous user agents, malformed status codes, response-size variations, and geographic telemetry.

---

## 🏗️ System Architecture & Workflow

1. **Ingestion & Sanitation:** Ingests network web-traffic logs, automatically scrubbing high-complexity fields to maintain structural schema integrity.
2. **Feature Engineering Dynamic:** Extracts explicit time-of-day dynamics, flags automated API calls, and standardizes continuous distributions (e.g., response times, error rates) to stabilize variance.
3. **Isolation Modeling:** Evaluates the continuous feature matrix to identify data points that isolate quickly deep within the decision trees.
4. **SHAP Explanation Translation:** Computes Shapley values for isolated outliers, quantifying exactly how much each parameter contributed to the anomaly score.
5. **UI Rendering:** Builds dynamic, interactive plots directly in the web browser using Streamlit and Matplotlib.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** Streamlit (Frontend & Application Layer)
* **Machine Learning:** Scikit-Learn (Isolation Forest, Preprocessing)
* **Model Explainability:** SHAP
* **Data Engineering:** Pandas, NumPy
* **Visualization:** Matplotlib

---

## 📦 Project Structure

```text
├── Unsupervised Anomaly Detection.ipynb  # Core R&D notebook for model prototyping & validation
├── app.py                                # Main Streamlit web application & compute pipeline
├── requirements.txt                      # Python dependencies package manifest
├── telecom_web_logs_dataset.csv          # Telecom web log dataset used by the pipeline
└── README.md                             # System documentation
