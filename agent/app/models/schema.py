from pydantic import BaseModel


class LogRequest(BaseModel):
    service: str
    log: str


class QueryRequest(BaseModel):
    query: str
