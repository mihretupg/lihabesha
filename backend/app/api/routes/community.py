from fastapi import APIRouter

router = APIRouter(prefix="/community", tags=["community"])

@router.get("/")
def list_community():
    return {"items": []}
