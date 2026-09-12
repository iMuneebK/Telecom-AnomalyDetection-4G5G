# 🛡️ AI Network Anomaly Detection

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red.svg)
![IsolationForest](https://img.shields.io/badge/scikit--learn-AnomalyDetection-orange.svg)

AI-based Network Anomaly Detection System tailored for modern 4G/5G infrastructure security.

## 🔍 Features
- **Real-Time Detection**: Employs Autoencoders and Isolation Forest to identify anomalous traffic.
- **Threat Identification**: Detects DDoS attacks, unusual traffic patterns, and potential equipment failures.
- **Time-Series Analysis**: Monitors network metrics including latency spikes, throughput drops, and jitter.
- **Alerting & Visualization**: Automated severity classification with a sleek Plotly/Streamlit dashboard.

## 🛡️ Securing Modern Telecom
As telecom networks scale, traditional rule-based firewalls fall short. This AI solution learns the "normal" behavior of network traffic and instantly flags deviations, ensuring high availability and secure communications for 5G infrastructure.

## 🚀 Usage
```bash
pip install -r requirements.txt
streamlit run app.py
```\n