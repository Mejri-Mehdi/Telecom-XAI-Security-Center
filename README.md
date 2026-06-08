# 🛡️ Enterprise Telecom XAI Security Center

An Explainable Artificial Intelligence (XAI) threat detection pipeline designed to safeguard telecommunications network infrastructure. This production-ready web application baselines normal operations using an Unsupervised **Isolation Forest** model to detect sophisticated anomalies, then mathematically decodes and translates them into human-readable Threat Intelligence using **SHAP (SHapley Additive exPlanations)**.

Live dashboards are built with **Streamlit** and optimized for security analysts requiring immediate context behind automated security flags.

---

## 🚀 Key Features

* **Unsupervised Anomaly Detection:** Leverages an Isolation Forest engine to detect zero-day threats, multi-vector attacks, and infrastructure anomalies without requiring pre-labeled training data.
* **Explainable AI (XAI) Core:** Converts the complex internal decision-making process of the ML model into exact feature-attribution charts via SHAP values, showing analysts *why* a specific log entry was flagged.
* **Production-Grade Data Pipeline:** Built-in multi-stage feature engineering, automated label encoding, and robust data standardization using Scikit-Learn.
* **Interactive Analyst Dashboard:** A scannable visual command center allowing real-time inspection of anomalous user agents, malformed status codes, response-size variations, and geographic telemetry.

---

## 🏗️ System Architecture & Workflow

1. **Ingestion & Sanitation:** Ingests raw network web-traffic logs, automatically scrubbing high-complexity fields (such as nested JSON data) to maintain structural schema integrity.
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
├── app.py                      # Main Streamlit web application & compute pipeline
├── cleaned_telecom_logs.csv    # Sanitized telecom log dataset (scrubbed features)
├── requirements.txt            # Python dependencies package manifest
└── README.md                   # System documentation
