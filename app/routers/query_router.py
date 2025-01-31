# backend/app/routers/query_router.py

from fastapi import APIRouter, HTTPException
from app.services.nlp_service import NLPService
from app.schemas.query_schema import QueryRequest, QueryResponse

router = APIRouter()

# Initialize the NLP service
nlp_service = NLPService()

@router.post("/generate-sql", response_model=QueryResponse)
async def generate_sql(query_request: QueryRequest):
    """
    Endpoint to generate an SQL query from a natural language query.
    """
    try:
        sql_query = nlp_service.generate_sql_query(query_request.user_query)
        return QueryResponse(sql_query=sql_query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))