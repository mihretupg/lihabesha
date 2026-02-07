from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.post import HousingPostCreate, PostPublic, PostUpdate
from app.services import post_service
from app.core.security import get_current_user

router = APIRouter(prefix="/housing", tags=["housing"])


@router.get("/", response_model=list[PostPublic])
def list_housing(
    city: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return post_service.list_posts(
        db,
        post_type="housing",
        city=city,
        min_price=min_price,
        max_price=max_price,
        limit=limit,
        offset=offset,
    )


@router.post("/", response_model=PostPublic)
def create_housing(
    payload: HousingPostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return post_service.create_post(
        db,
        post_type="housing",
        title=payload.title,
        description=payload.description,
        owner_id=current_user.id,
        city=payload.city,
        price=payload.price,
        availability_date=payload.availability_date,
        room_type=payload.room_type,
    )


@router.patch("/{post_id}", response_model=PostPublic)
def update_housing(
    post_id,
    payload: PostUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    post = post_service.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id and current_user.role not in {"admin", "moderator"}:
        raise HTTPException(status_code=403, detail="Forbidden")
    return post_service.update_post(db, post, **payload.model_dump())


@router.delete("/{post_id}")
def delete_housing(
    post_id,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    post = post_service.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id and current_user.role not in {"admin", "moderator"}:
        raise HTTPException(status_code=403, detail="Forbidden")
    post_service.delete_post(db, post)
    return {"status": "deleted"}
