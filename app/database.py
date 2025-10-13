from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# ✅ Create SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# ✅ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Provide helper functions
def get_engine():
    return engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

