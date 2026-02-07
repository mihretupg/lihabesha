from fastapi import APIRouter

router = APIRouter(prefix="/travel", tags=["travel"])

@router.get("/")
def list_travel():
    return {"items": []}
