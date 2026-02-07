from fastapi import APIRouter

router = APIRouter(prefix="/housing", tags=["housing"])

@router.get("/")
def list_housing():
    return {"items": []}
