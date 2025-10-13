from dash_extensions.enrich import DashProxy, MultiplexerTransform
from dash import html, dcc
from fastapi import FastAPI

# Use the existing FastAPI server
from app.main import app as server

# Correct url_base_pathname
dash_app = DashProxy(
    __name__,
    server=server,
    url_base_pathname="/dashboard/",  # Trailing slash is important
    transforms=[MultiplexerTransform()],
)

dash_app.layout = html.Div([
    html.H1("Database Monitoring Dashboard"),
    dcc.Graph(id="sample-graph")
])

# Optional: Add callbacks here
