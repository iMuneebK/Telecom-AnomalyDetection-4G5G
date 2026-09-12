from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        # Using Isolation Forest as a proxy for the ensemble
        self.model = IsolationForest(contamination=0.1, random_state=42)
        # Mock fit on normal data
        X_train = np.random.normal(loc=[20, 100], scale=[2, 10], size=(1000, 2))
        self.model.fit(X_train)

    def detect(self, data_point):
        X = np.array([[data_point['latency'], data_point['throughput']]])
        pred = self.model.predict(X)
        return pred[0] == -1 # -1 is anomaly in IsolationForest\n