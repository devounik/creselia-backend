# backend/app/schemas/query_schema.py

from pydantic import BaseModel

class QueryRequest(BaseModel):
    """
    Request model for the natural language query.
    """
    user_query: str

class QueryResponse(BaseModel):
    """
    Response model for the generated SQL query.
    """
    sql_query: str