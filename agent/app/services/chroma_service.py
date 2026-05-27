import chromadb

from app.config import settings

_client = chromadb.PersistentClient(path=settings.chroma_path)

collection = _client.get_or_create_collection(name=settings.chroma_collection)
