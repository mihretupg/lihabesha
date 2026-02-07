from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.post import TravelPostCreate, PostPublic, PostUpdate
from app.services import post_service
from app.core.security import get_current_user

router = APIRouter(prefix="/travel", tags=["travel"])


@router.get("/", response_model=list[PostPublic])
def list_travel(
    city: str | None = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return post_service.list_posts(
        db,
        post_type="travel",
        city=city,
        limit=limit,
        offset=offset,
    )


@router.post("/", response_model=PostPublic)
def create_travel(
    payload: TravelPostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return post_service.create_post(
        db,
        post_type="travel",
        title=payload.title,
        description=payload.description,
        owner_id=current_user.id,
        city=payload.city,
        price=payload.price,
        travel_date=payload.travel_date,
        route=payload.route,
    )


@router.patch("/{post_id}", response_model=PostPublic)
def update_travel(
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
def delete_travel(
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
