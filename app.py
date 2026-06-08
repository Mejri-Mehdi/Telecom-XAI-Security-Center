import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler, LabelEncoder

# ==============================================================================
# 0. GLOBAL PAGE SETTINGS & STYLING
# ==============================================================================
st.set_page_config(
    page_title="Telecom XAI Security Center", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for minor spacing improvements and cleaner typography
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Enterprise Telecom XAI Security Center")
st.markdown("""
**Explainable Artificial Intelligence (XAI) Threat Detection Pipeline** This production system baselines normal operations using an Unsupervised **Isolation Forest**. 
Anomalies are mathematically decapped and translated into human-readable Threat Intelligence using **SHAP**.
""")

# ==============================================================================
# 1. PERFORMANCE OPTIMIZED COMPUTE PIPELINE
# ==============================================================================
@st.cache_resource(show_spinner="Initializing AI Security Models...")
def run_security_pipeline(file_path):
    # Load raw telemetry data
    df = pd.read_csv(file_path)
    df_processed = df.copy()
    
    # Feature Engineering
    df_processed['timestamp'] = pd.to_datetime(df_processed['timestamp'])
    df_processed['hour_of_day'] = df_processed['timestamp'].dt.hour
    
    cols_to_drop = ['timestamp', 'session_id', 'threat_type', 'is_malicious', 'related_session', 'correlation_type', 'http_headers']
    df_processed = df_processed.drop(columns=cols_to_drop, errors='ignore')
    
    categorical_cols = ['ip_address', 'user_agent', 'http_method', 'endpoint', 'device_type', 'user_role', 'country', 'city', 'asn', 'isp']
    for col in categorical_cols:
        if col in df_processed.columns:
            le = LabelEncoder()
            df_processed[col] = le.fit_transform(df_processed[col].astype(str))
            
    # Clean zero-variance features
    cols_to_drop_variance = [col for col in df_processed.columns if df_processed[col].nunique() <= 1]
    df_processed = df_processed.drop(columns=cols_to_drop_variance)
    
    # Scale Data
    numerical_cols = [c for c in ['status_code', 'response_size', 'request_duration_ms', 'error_rate', 'hour_of_day', 'is_api'] if c in df_processed.columns]
    scaler = StandardScaler()
    df_processed[numerical_cols] = scaler.fit_transform(df_processed[numerical_cols])
    
    # Train AI Model
    iso_forest = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    iso_forest.fit(df_processed) 
    
    # Generate Predictions
    predictions = iso_forest.predict(df_processed)
    scores = iso_forest.decision_function(df_processed)
    
    df['anomaly_score'] = scores
    df['is_anomaly'] = predictions
    
    # Extract SHAP Values
    explainer = shap.TreeExplainer(iso_forest)
    anomaly_indices = df[df['is_anomaly'] == -1].index
    anomalies_scaled = df_processed.loc[anomaly_indices]
    shap_values = explainer.shap_values(anomalies_scaled)
    
    return df, df_processed, anomaly_indices, anomalies_scaled, shap_values, explainer

# Execute analytics
file_name = 'telecom_web_logs_dataset.csv'
try:
    df, df_processed, anomaly_indices, anomalies_scaled, shap_values, explainer = run_security_pipeline(file_name)
except Exception as e:
    st.error(f"❌ Initialization Failed. Please confirm that '{file_name}' resides in your execution folder. Error Details: {e}")
    st.stop()

# Prepare Anomaly Tracking Dataframe
all_anomalies_df = df[df['is_anomaly'] == -1].copy()
all_anomalies_df['anomaly_tracking_id'] = range(len(all_anomalies_df))
all_anomalies_df['original_row_index'] = all_anomalies_df.index + 1

# ==============================================================================
# 2. HIGH-LEVEL SOC EXECUTIVE METRICS (Visual Cards)
# ==============================================================================
st.header("Executive Summary", divider="blue")

with st.container(border=True):
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric("📡 Total Logs Processed", f"{len(df):,}")
    with m_col2:
        st.metric("✅ Normal Baseline Traffic", f"{len(df[df['is_anomaly'] == 1]):,}")
    with m_col3:
        st.metric("🚨 Isolated Threat Alerts", f"{len(all_anomalies_df):,}", delta="-1.0% Contamination Rate", delta_color="inverse")

# ==============================================================================
# 3. INTERACTIVE INCIDENT FORENSICS
# ==============================================================================
st.header("🔬 Dynamic Incident Forensics", divider="blue")

# --- CONTROL PANEL ---
with st.container(border=True):
    st.markdown("##### 🎛️ Investigation Control Panel")
    selected_id = st.selectbox(
        "Select an Isolated Threat ID to decode its AI signature:",
        options=all_anomalies_df['anomaly_tracking_id'].tolist(),
        format_func=lambda x: f"Threat ID #{x} — Source IP: {all_anomalies_df.iloc[x]['ip_address']} — {all_anomalies_df.iloc[x]['timestamp'][:10]}"
    )

# Extract Context
actual_index = anomaly_indices[selected_id]
original_anomaly = df.loc[actual_index]
scaled_row = df_processed.loc[actual_index]

if isinstance(shap_values, list):
    row_shap = shap_values[0][selected_id]
else:
    row_shap = shap_values[selected_id]

top_feature_indices = np.argsort(np.abs(row_shap))[::-1][:2]
trigger_1_name = df_processed.columns[top_feature_indices[0]]
trigger_2_name = df_processed.columns[top_feature_indices[1]]

trigger_1_value = original_anomaly.get(trigger_1_name, scaled_row[trigger_1_name])
trigger_2_value = original_anomaly.get(trigger_2_name, scaled_row[trigger_2_name])

threat_intel_db = {
    'status_code': "Abnormal HTTP status behavior indicates systemic endpoint probing, exploitation attempts, or forced-error application crashes.",
    'error_rate': "Elevated resource error rates are consistent with rapid automated dictionary-attacks, directory fuzzing, or brute-forcing scripts.",
    'response_size': "Significant payload deviations point toward targeted data exfiltration attempts or heavy payload injection feedback loops.",
    'request_duration_ms': "Anomalous latency patterns indicate injection-heavy calculations, remote command executions, or denial-of-service stress tests.",
    'hour_of_day': "Unusual time-of-day activity flags cron-scheduled botnet activity or cross-timezone adversary attacks outside normal working parameters.",
    'device_type': "Non-standard or headless client profiles indicate customized exploitation toolsets, spoofed web headers, or crawler activity.",
    'user_role': "Privilege context boundaries variations imply lateral migration attempts or access privilege escalation testing.",
    'country': "Unexpected source geolocations represent suspicious proxy rerouting, commercial VPN tunneling infrastructure, or rogue bot clusters.",
    'endpoint': "Targeting critical administrative interfaces or uncommon parameters implies highly focused security reconnaissance.",
    'http_method': "Uncommon or forced HTTP methods highlight REST API structural abuse or attempt to bypass web application filters.",
    'ip_address': "Severe structural distance from baseline tracking flags persistent hostile nodes targeting infrastructure systems.",
    'user_agent': "Mismatched browser fingerprints confirm automated scrapers, raw python requests, or headless execution testing.",
    'city': "Anomalous city tracking vectors indicate coordinated distributed botnets targeting localized entry boundaries.",
    'asn': "Autonomous System Number routing deviations prove request flows originate from hostile data-center nodes rather than valid consumer paths.",
    'isp': "Hostile provider routing points to known bad host hosting nodes, unverified cloud servers, or darknet entry proxies.",
    'is_api': "Sudden pivots toward raw application program interfaces reveal automated endpoints exploitation patterns."
}

explanation_1 = threat_intel_db.get(trigger_1_name, "Anomalous variation from normal feature cluster signature.")
explanation_2 = threat_intel_db.get(trigger_2_name, "Anomalous variation from normal feature cluster signature.")

# --- DISPLAY THE FORENSICS ---
col_report, col_chart = st.columns([1.1, 0.9], gap="large")

with col_report:
    st.markdown(f"### 📋 Threat Profile Report")
    st.warning(f"**Tracking ID:** #{selected_id} &nbsp;|&nbsp; **Dataset Row:** {actual_index + 1}")
    
    # Triggers in a beautiful red error box
    st.error(f"""
    **🚨 PRIMARY BEHAVIORAL TRIGGERS** The AI isolated this network request specifically because of these two factors:
    
    1️⃣ **{trigger_1_name.upper()}** (`{trigger_1_value}`)  
    *Intelligence:* {explanation_1}
    
    2️⃣ **{trigger_2_name.upper()}** (`{trigger_2_value}`)  
    *Intelligence:* {explanation_2}
    """)
    
    # Beautiful Grid for Traffic Metadata
    st.markdown("#### 🌐 Traffic Metadata Context")
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"**Target IP**<br>`{original_anomaly['ip_address']}`", unsafe_allow_html=True)
        c2.markdown(f"**Location**<br>`{original_anomaly['country']} ({original_anomaly['city']})`", unsafe_allow_html=True)
        c3.markdown(f"**Network / ISP**<br>`{original_anomaly['isp']}`", unsafe_allow_html=True)
        
        st.divider()
        
        c4, c5, c6 = st.columns(3)
        c4.markdown(f"**Access URI**<br>`{original_anomaly['http_method']} {original_anomaly['endpoint']}`", unsafe_allow_html=True)
        c5.markdown(f"**Status Code**<br>`{original_anomaly['status_code']}`", unsafe_allow_html=True)
        c6.markdown(f"**Client Type**<br>`{original_anomaly['device_type']} ({original_anomaly['user_role']})`", unsafe_allow_html=True)
        
        st.divider()
        
        c7, c8, c9 = st.columns(3)
        c7.markdown(f"**Payload Size**<br>`{original_anomaly['response_size']} bytes`", unsafe_allow_html=True)
        c8.markdown(f"**Latency**<br>`{original_anomaly['request_duration_ms']} ms`", unsafe_allow_html=True)
        c9.markdown(f"**Timestamp**<br>`{original_anomaly['timestamp']}`", unsafe_allow_html=True)

with col_chart:
    st.markdown("### 📊 AI Decision Breakdown (SHAP)")
    st.info("💡 **How to read:** Red arrows push the risk score higher (Threat). Blue arrows pull the score lower (Normal).")
    st.info("""
    💡 **How to read an Isolation Forest plot:** The chart starts at a high 'Normal' baseline. **Blue arrows** subtract normality points, 
    pulling the score down into the negative **Anomaly/Threat** zone. Therefore, the longest 
    blue bars represent the features driving the threat.
    """)
    
    with st.container(border=True):
        plt.style.use('default')
        base_val = explainer.expected_value[0] if isinstance(explainer.expected_value, list) else explainer.expected_value
        explanation = shap.Explanation(
            values=row_shap, 
            base_values=base_val, 
            data=scaled_row, 
            feature_names=df_processed.columns
        )
        
        shap.plots.waterfall(explanation, show=False)
        fig = plt.gcf()
        fig.patch.set_facecolor('white')  
        fig.patch.set_alpha(1.0)          
        
        for ax in fig.axes:
            ax.set_facecolor('white')     
            ax.xaxis.label.set_color('black')
            ax.yaxis.label.set_color('black')
            ax.tick_params(colors='black', which='both')
        
        st.pyplot(fig, use_container_width=True)
        plt.clf()
        plt.close(fig)

# ==============================================================================
# 4. MASTER AUDIT LEDGER VIEW
# ==============================================================================
st.header("🗄️ Security Alert Ledger", divider="blue")
st.markdown("Historical index of all isolated logs for batch review. Click any column header to sort.")

ledger_cols = ['anomaly_tracking_id', 'original_row_index', 'ip_address', 'country', 'device_type', 'user_role', 'endpoint', 'status_code', 'response_size', 'request_duration_ms']

with st.container(border=True):
    st.dataframe(
        all_anomalies_df[ledger_cols],
        use_container_width=True,
        hide_index=True,
        height=400
    )