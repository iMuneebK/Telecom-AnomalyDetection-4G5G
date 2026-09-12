import streamlit as st
import pandas as pd
import time
from data_generator import generate_traffic_stream
from anomaly_detector import AnomalyDetector
from visualizer import plot_traffic_health

st.set_page_config(page_title="Network Anomaly Detection", layout="wide")
st.title("🛡️ AI-Based Network Anomaly Detection System")
st.markdown("Real-time monitoring of 4G/5G infrastructure for DDoS attacks and equipment failures.")

detector = AnomalyDetector()

if st.button("Start Real-Time Monitoring"):
    placeholder = st.empty()
    alert_box = st.empty()
    stream = generate_traffic_stream()

    history = []
    for i in range(50):
        data = next(stream)
        is_anomaly = detector.detect(data)
        data['anomaly'] = is_anomaly
        history.append(data)

        df = pd.DataFrame(history)

        if is_anomaly:
            alert_box.error(f"⚠️ ANOMALY DETECTED at T={data['time']}! High risk of DDoS or Failure.")
        else:
            alert_box.success("✅ Network Health Normal")

        placeholder.plotly_chart(plot_traffic_health(df), use_container_width=True)
        time.sleep(0.5)\n