import uuid

from fastapi import APIRouter

from app.models.schema import LogRequest
from app.services.chroma_service import collection
from app.services.embedding_service import encode

router = APIRouter()


@router.post("/ingest")
async def ingest_log(data: LogRequest):
    collection.add(
        ids=[str(uuid.uuid4())],
        documents=[data.log],
        embeddings=[encode(data.log)],
        metadatas=[{"service": data.service}],
    )
    return {"status": "stored"}
