import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df: pd.DataFrame):
    if df.empty:
        return []
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['execution_time']])
    anomalies = df[df['anomaly'] == -1]
    return anomalies.to_dict(orient='records')