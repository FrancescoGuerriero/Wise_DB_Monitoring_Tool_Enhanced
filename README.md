# Wise DB Monitoring Tool

Python-based DB monitoring with ML anomaly detection and auto-indexing.

Use `python -m app.init_db` to initialize database with sample data.

Run server: `uvicorn app.main:app --reload`

Endpoints:
- GET /query-stats
- GET /anomalies
- GET /auto-index