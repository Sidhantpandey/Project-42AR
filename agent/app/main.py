from fastapi import FastAPI

from app.routes import api_router

app = FastAPI(title="RAG Service")

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "RAG Service Running"}
