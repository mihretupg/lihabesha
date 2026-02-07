from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="Lihabesha API")

app.include_router(api_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
