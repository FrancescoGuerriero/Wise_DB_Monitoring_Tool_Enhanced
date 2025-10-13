from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
DATABASE_URL = "postgresql+psycopg2://postgres:yourpassword@localhost:5432/yourdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class ServerMetrics(Base):
    __tablename__ = "server_metrics"
    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String, default="local_server")
    cpu = Column(Float)
    memory = Column(Float)
    disk = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Alerts(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String)
    alert_type = Column(String)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

    def get_server_metrics(limit=10):
    session = SessionLocal()
    metrics = session.query(ServerMetrics).order_by(ServerMetrics.timestamp.desc()).limit(limit).all()
    session.close()
    return metrics

def get_alerts(limit=10):
    session = SessionLocal()
    alerts = session.query(Alerts).order_by(Alerts.timestamp.desc()).limit(limit).all()
    session.close()
    return alerts

