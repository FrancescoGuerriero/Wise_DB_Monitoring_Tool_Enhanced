import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
from app.db import get_server_metrics, get_alerts
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Server Monitoring Dashboard"),

    html.H2("Server Metrics"),
    dash_table.DataTable(
        id='metrics-table',
        columns=[
            {"name": "Timestamp", "id": "timestamp"},
            {"name": "CPU (%)", "id": "cpu"},
            {"name": "Memory (%)", "id": "memory"},
            {"name": "Disk (%)", "id": "disk"}
        ],
        data=[],
        style_cell={'textAlign': 'center'},
        style_header={'fontWeight': 'bold'},
    ),

    html.H2("Alerts"),
    dash_table.DataTable(
        id='alerts-table',
        columns=[
            {"name": "Timestamp", "id": "timestamp"},
            {"name": "Server", "id": "server_name"},
            {"name": "Type", "id": "alert_type"},
            {"name": "Description", "id": "description"}
        ],
        data=[],
        style_cell={'textAlign': 'center'},
        style_header={'fontWeight': 'bold'},
    ),

    dcc.Interval(
        id='interval-component',
        interval=5000,  # refresh every 5 seconds
        n_intervals=0
    )
])

@app.callback(
    Output('metrics-table', 'data'),
    Output('alerts-table', 'data'),
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    metrics = get_server_metrics()
    alerts = get_alerts()
    metrics_data = [{"timestamp": m.timestamp, "cpu": m.cpu, "memory": m.memory, "disk": m.disk} for m in metrics]
    alerts_data = [{"timestamp": a.timestamp, "server_name": a.server_name, "alert_type": a.alert_type, "description": a.description} for a in alerts]
    return metrics_data, alerts_data
