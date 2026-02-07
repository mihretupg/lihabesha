from fastapi import APIRouter

router = APIRouter(prefix="/moderation", tags=["moderation"])

@router.get("/reports")
def list_reports():
    return {"items": []}
