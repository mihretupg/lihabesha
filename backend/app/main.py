from fastapi import FastAPI

app = FastAPI(title="Lihabesha API")

@app.get("/health")
def health():
    return {"status": "ok"}
