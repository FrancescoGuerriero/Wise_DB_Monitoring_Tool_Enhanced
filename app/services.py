# app/services.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from .config import settings
import pandas as pd

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_query_stats():
    query = """
    SELECT
        COUNT(*) AS total_queries,
        AVG(execution_time) AS avg_execution_time,
        MAX(execution_time) AS max_execution_time,
        MIN(execution_time) AS min_execution_time
    FROM query_logs;
    """
    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().first()
    return dict(result) if result else {"total_queries":0,"avg_execution_time":0,"max_execution_time":0,"min_execution_time":0}

def get_anomalies(threshold_ms=500):
    query = text("SELECT query, execution_time, timestamp FROM query_logs WHERE execution_time > :threshold")
    with SessionLocal() as session:
        result = session.execute(query, {"threshold": threshold_ms}).mappings().all()
    return [dict(r) for r in result]

def get_auto_index_suggestions():
    return [
        {"table":"users","column":"email","suggestion":"CREATE INDEX idx_users_email ON users(email);"},
        {"table":"orders","column":"created_at","suggestion":"CREATE INDEX idx_orders_created_at ON orders(created_at);"}
    ]
