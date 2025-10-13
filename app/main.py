from fastapi.responses import RedirectResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/dashboard")
def redirect_dashboard():
    return RedirectResponse(url="/dashboard/")
