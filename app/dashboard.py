# Use absolute import
from app.config import settings
import dash
from dash import html
from dash_extensions.enrich import send_data_frame  # type: ignore

def create_dashboard():
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1("Database Monitoring Dashboard"),
        html.P("This is your FastAPI + Dash dashboard.")
    ])
    return app

