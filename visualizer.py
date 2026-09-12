import plotly.graph_objects as go

def plot_traffic_health(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['time'], y=df['latency'], mode='lines+markers', name='Latency (ms)',
                             marker=dict(color=df['anomaly'].map({True: 'red', False: 'blue'}))))
    fig.update_layout(title="Real-Time Network Latency", template="plotly_dark")
    return fig\n