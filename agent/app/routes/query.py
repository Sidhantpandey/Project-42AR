from fastapi import APIRouter

from app.config import settings
from app.models.schema import QueryRequest
from app.services.chroma_service import collection
from app.services.embedding_service import encode

router = APIRouter()


@router.post("/query")
async def query_logs(data: QueryRequest):
    results = collection.query(
        query_embeddings=[encode(data.query)],
        n_results=settings.query_n_results,
    )
    return results
