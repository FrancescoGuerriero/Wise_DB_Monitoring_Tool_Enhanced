from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, nullable=False)
    execution_time = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
