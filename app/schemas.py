from pydantic import BaseModel

class QueryLogBase(BaseModel):
    query: str
    execution_time: int
    timestamp: int

class QueryLog(QueryLogBase):
    id: int
    class Config:
        orm_mode = True