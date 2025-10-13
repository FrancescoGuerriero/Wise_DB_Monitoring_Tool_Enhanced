import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
from dash_extensions.enrich import Output, Input, DashProxy
import pandas as pd
import random
from datetime import datetime

# -------------------------------
# Dummy DB functions (replace with app.db later)
# -------------------------------
def get_server_metrics():
    """Simulate server metrics"""
    return [
        {"server": "Server1", "cpu": random.randint(0, 100), "memory": random.randint(0, 100), "timestamp": datetime.now()},
        {"server": "Server2", "cpu": random.randint(0, 100), "memory": random.randint(0, 100), "timestamp": datetime.now()},
    ]

def get_alerts():
    """Simulate alerts"""
    alerts = []
    for server in ["Server1", "Server2"]:
        if random.random() > 0.7:  # 30% chance of alert
            alerts.append({"server": server, "alert": "High CPU usage", "timestamp": datetime.now()})
    return alerts

# -------------------------------
# Initialize Dash app
# -------------------------------
dash_app = DashProxy(__name__)
dash_app.layout = html.Div([
    html.H1("Server Monitoring Dashboard"),
    dcc.Interval(id="interval-component", interval=5000, n_intervals=0),  # refresh every 5s

    html.H2("Server Metrics"),
    dash_table.DataTable(
        id='metrics-table',
        columns=[
            {"name": "Server", "id": "server"},
            {"name": "CPU (%)", "id": "cpu"},
            {"name": "Memory (%)", "id": "memory"},
            {"name": "Timestamp", "id": "timestamp"},
        ],
        style_data_conditional=[],
        style_cell={"textAlign": "center"}
    ),

    html.H2("Active Alerts"),
    dash_table.DataTable(
        id='alerts-table',
        columns=[
            {"name": "Server", "id": "server"},
            {"name": "Alert", "id": "alert"},
            {"name": "Timestamp", "id": "timestamp"},
        ],
        style_data_conditional=[],
        style_cell={"textAlign": "center"}
    )
])

# -------------------------------
# Callbacks
# -------------------------------
@dash_app.callback(
    Output('metrics-table', 'data'),
    Output('metrics-table', 'style_data_conditional'),
    Input('interval-component', 'n_intervals')
)
def update_metrics(n):
    metrics = get_server_metrics()
    for m in metrics:
        m['timestamp'] = m['timestamp'].strftime("%H:%M:%S")

    style_conditional = []
    for i, row in enumerate(metrics):
        if row["cpu"] > 80:
            style_conditional.append({
                "if": {"row_index": i, "column_id": "cpu"},
                "backgroundColor": "tomato",
                "color": "white"
            })
        if row["memory"] > 80:
            style_conditional.append({
                "if": {"row_index": i, "column_id": "memory"},
                "backgroundColor": "orange",
                "color": "white"
            })
    return metrics, style_conditional

@dash_app.callback(
    Output('alerts-table', 'data'),
    Output('alerts-table', 'style_data_conditional'),
    Input('interval-component', 'n_intervals')
)
def update_alerts(n):
    alerts = get_alerts()
    for a in alerts:
        a['timestamp'] = a['timestamp'].strftime("%H:%M:%S")

    style_conditional = []
    for i, row in enumerate(alerts):
        style_conditional.append({
            "if": {"row_index": i},
            "backgroundColor": "red",
            "color": "white"
        })
    return alerts, style_conditional


