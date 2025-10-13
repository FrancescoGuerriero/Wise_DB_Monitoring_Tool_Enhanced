# app/main.py
from fastapi import FastAPI
from dash import Dash
from dash_app.dashboard import create_dashboard
 # your dashboard factory

# FastAPI app
app = FastAPI(title="Wise DB Monitoring Tool")

# Create Dash dashboard inside FastAPI
dash_app = create_dashboard(app)

# Optional: simple root endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI + Dash app running!"}
