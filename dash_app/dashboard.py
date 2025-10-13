import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from app.database import get_engine

def create_dashboard():
    app = dash.Dash(__name__, requests_pathname_prefix="/", suppress_callback_exceptions=True)
    engine = get_engine()

    # Example query
    query = "SELECT * FROM query_logs LIMIT 100"
    df = pd.read_sql(query, engine)

    app.layout = html.Div([
        html.H1("📊 Wise Database Monitoring Dashboard"),
        dcc.Dropdown(
            id="metric",
            options=[{"label": c, "value": c} for c in df.columns if df[c].dtype != "object"],
            value=df.columns[0],
            clearable=False
        ),
        dcc.Graph(id="graph")
    ])

    @app.callback(
        Output("graph", "figure"),
        Input("metric", "value")
    )
    def update_graph(metric):
        fig = px.histogram(df, x=metric, title=f"Distribution of {metric}")
        return fig

    return app
