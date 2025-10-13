from fastapi import FastAPI
from dash_app.dashboard import create_dashboard
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI(title="Wise DB Monitoring Tool")

# Mount Dash dashboard
dash_app = create_dashboard()
app.mount("/", WSGIMiddleware(dash_app.server))


