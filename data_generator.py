import numpy as np

def generate_traffic_stream():
    t = 0
    while True:
        t += 1
        # Inject anomalies 10% of the time
        if np.random.rand() < 0.1:
            yield {"time": t, "latency": np.random.normal(200, 50), "throughput": np.random.normal(10, 5)} # anomaly
        else:
            yield {"time": t, "latency": np.random.normal(20, 2), "throughput": np.random.normal(100, 10)} # normal\n