from dash_extensions.enrich import DashProxy, Output, Input, MultiplexerTransform
from dash import html, dcc
import pandas as pd

def create_dashboard(server):
    """
    Create a Dash dashboard and attach it to the FastAPI server.
    """
    # Use DashProxy with transforms to allow multiple callbacks
    dash_app = DashProxy(
        __name__,
        server=server,       # FastAPI app
        url_base_pathname="/dashboard/",
        transforms=[MultiplexerTransform()],
    )

    # Example layout
    dash_app.layout = html.Div([
        html.H1("Database Monitoring Dashboard"),
        html.Button("Load Sample Data", id="load-btn"),
        html.Div(id="table-container")
    ])

    # Example callback
    @dash_app.callback(
        Output("table-container", "children"),
        Input("load-btn", "n_clicks")
    )
    def load_data(n_clicks):
        if not n_clicks:
            return "Click the button to load data."
        # Example DataFrame
        df = pd.DataFrame({
            "Metric": ["CPU Usage", "Memory Usage", "Connections"],
            "Value": [20, 50, 10]
        })
        return html.Table([
            html.Tr([html.Th(col) for col in df.columns])] +
            [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
        )

    return dash_app

