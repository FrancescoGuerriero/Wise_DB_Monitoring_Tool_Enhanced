from datetime import datetime
from sqlalchemy.orm import Session
from app.models import QueryLog  # or your table model
from app.database import engine

# Example data
query_logs_data = [
    {'query': 'SELECT * FROM users', 'execution_time': 120, 'timestamp': 1697100000},
    {'query': 'SELECT * FROM orders WHERE user_id=1', 'execution_time': 200, 'timestamp': 1697100300},
    # Add more entries...
]

with Session(engine) as db:
    for entry in query_logs_data:
        timestamp_dt = datetime.fromtimestamp(entry['timestamp'])  # Convert UNIX int -> datetime
        log = QueryLog(
            query=entry['query'],
            execution_time=entry['execution_time'],
            timestamp=timestamp_dt
        )
        db.add(log)
    db.commit()

print("Database initialized successfully!")
