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

## 📸 Production Dashboard & Threat Intelligence Visualizations

The Enterprise Telecom XAI Security Center delivers an interactive, production-grade visual interface for security operations center (SOC) analysts. Below is the architectural breakdown of the dashboard across its four primary analytical modules:

<div align="center">

### 1. Global Security Command Center & Baseline Traffic Monitoring
<img src="https://github.com/user-attachments/assets/1009bebd-c4e3-43e5-886f-d06a624bf0eb" alt="Global Security Command Center" width="850"/>

📋 **Operational Telemetry Monitoring**
* **High-Level KPI Tracking:** Provides immediate visibility into total analyzed telecom network logs, live system health indicators, and real-time malicious traffic thresholds.
* **Ingestion Verification:** Monitors the behavioral baseline of incoming web requests across active network endpoints, request duration scales, and server status codes.

---

### 2. Unsupervised Outlier Detection & Anomaly Distribution Matrix
<img src="https://github.com/user-attachments/assets/1356862a-256a-4818-959e-ceca994ab61b" alt="Isolation Forest Anomaly Scoring" width="850"/>

🌲 **Isolation Forest Decision Segments**
* **Mathematical Isolation Scoring:** Displays the multi-dimensional feature space distribution where malicious data points are separated based on their tree path lengths.
* **Contamination Cutoff:** Clearly marks the custom **1%** contamination boundary, isolating high-risk outliers from normal telecom operation profiles.

---

### 3. Explainable AI (XAI) Core: SHAP Feature Attribution
<img src="https://github.com/user-attachments/assets/c19fdf17-d1ae-49aa-be3e-840aa850106e" alt="SHAP Explainable AI Summary Plot" width="850"/>

🧠 **Algorithmic Transparency Layer**
* **Root-Cause Determination:** Unlocks the machine learning black box by calculating exact Shapley values for flagged network anomalies.
* **Feature Contribution Analysis:** Quantifies precisely how individual parameters—such as atypical `user_agent` fingerprints, suspicious `http_method` patterns, or spiked `request_duration_ms` timings—influenced the security alert.

---

### 4. Interactive Threat Forensics & Telemetry Logs
<img src="https://github.com/user-attachments/assets/e9c36fda-b87c-423a-9b84-fe9a34647e92" alt="Threat Intelligence Deep-Dive Telemetry" width="850"/>

🔍 **Granular Incident Investigation**
* **Comprehensive Context Ingestion:** Displays detailed, filterable data tables mapped with critical telemetry including `ip_address`, `asn`, `isp`, `user_role`, and geographic location data.
* **DevSecOps Actionability:** Empowers engineering teams to rapidly extract exact telemetry signatures for automated firewall blacklisting, security patching, and targeted network blockades.

</div>
---

## 📦 Project Structure

```text
├── Unsupervised Anomaly Detection.ipynb  # Core R&D notebook for model prototyping & validation
├── app.py                                # Main Streamlit web application & compute pipeline
├── requirements.txt                      # Python dependencies package manifest
├── telecom_web_logs_dataset.csv          # Telecom web log dataset used by the pipeline
└── README.md                             # System documentation
```

<p align="center"> <sub>Built with ❤️ and XAI by <a href="https://github.com/Mejri-Mehdi">Mejri Mehdi</a></sub> </p>
