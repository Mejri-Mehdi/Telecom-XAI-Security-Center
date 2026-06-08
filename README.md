<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/SHAP-6E6E6E?style=for-the-badge&logo=shap&logoColor=white" alt="SHAP"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge" alt="Production"/>
</p>

<h1 align="center">🛡️ Enterprise Telecom XAI Security Center</h1>

<p align="center">
  <strong>An Explainable Artificial Intelligence (XAI) threat detection pipeline designed to safeguard telecommunications network infrastructure.<br>
  Detects zero‑day anomalies with Unsupervised Isolation Forest, then decodes them into human‑readable threat intelligence using SHAP.</strong>
</p>

<p align="center">
  <a href="https://telecom-xai-security-center-h2nvldw84vyk84kcylnvhk.streamlit.app">
    <img src="https://img.shields.io/badge/🚀_Launch_Live_App-Telecom_XAI_Security_Center-blue?style=for-the-badge" alt="Live Deployment"/>
  </a>
</p>

---

## 🔍 Overview

Modern telecom networks generate massive volumes of traffic logs that hide sophisticated, multi‑vector threats.  
**Enterprise Telecom XAI Security Center** solves this by combining:

- **Unsupervised Learning** – no need for labeled attack data; the Isolation Forest automatically flags anomalies.
- **Explainable AI** – SHAP values translate the model’s “black‑box” decisions into clear feature‑attribution charts, telling analysts **why** a log was flagged.

The result is a production‑ready, interactive dashboard that accelerates threat hunting and reduces false‑positive investigation time.

---

## 🚀 Key Features

| Feature | Description |
|---------|-------------|
| 🧠 **Unsupervised Anomaly Detection** | Isolation Forest engine catches zero‑day threats, multi‑vector attacks, and infrastructure drift – no pre‑labeled training data required. |
| 🔍 **Explainable AI Core** | SHAP values decode every anomaly, showing exactly how much each feature (user agent, response size, time of day, etc.) contributed to the alert. |
| ⚙️ **Production‑Grade Pipeline** | Multi‑stage feature engineering, automatic label encoding, and robust Scikit‑Learn standardization ensure consistent results. |
| 📊 **Interactive Analyst Dashboard** | Scannable visual command center for real‑time inspection of anomalous user agents, malformed status codes, response‑size spikes, and geographic telemetry. |

---

## 🏗️ System Architecture & Workflow

```text
           ┌──────────────────────┐
           │  Telecom Web Logs    │
           └──────────┬───────────┘
                      │ 1. Ingestion & Sanitation
                      ▼
           ┌──────────────────────┐
           │  Feature Engineering │
           │  (Time-of-day, API   │
           │   calls, scaling)    │
           └──────────┬───────────┘
                      │ 2. Feature Matrix
                      ▼
           ┌──────────────────────┐
           │  Isolation Forest    │
           │  (Anomaly Scoring)   │
           └──────────┬───────────┘
                      │ 3. Outlier Indices
                      ▼
           ┌──────────────────────┐
           │  SHAP Explainer      │
           │  (Feature Attribution)│
           └──────────┬───────────┘
                      │ 4. Explanation Values
                      ▼
           ┌──────────────────────┐
           │  Streamlit Dashboard │
           │  (Visualizations)    │
           └──────────────────────┘
