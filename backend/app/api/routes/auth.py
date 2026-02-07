from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register():
    return {"message": "register placeholder"}

@router.post("/login")
def login():
    return {"message": "login placeholder"}
