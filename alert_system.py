class AlertSystem:
    def classify_severity(self, anomaly_score):
        if anomaly_score > 0.8: return "CRITICAL"
        if anomaly_score > 0.5: return "HIGH"
        return "LOW"\n