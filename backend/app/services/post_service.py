from sqlalchemy.orm import Session
from app.models.post import Post


def list_posts(db: Session, *, post_type: str | None = None, city: str | None = None,
               min_price: float | None = None, max_price: float | None = None,
               limit: int = 50, offset: int = 0):
    query = db.query(Post)
    if post_type:
        query = query.filter(Post.post_type == post_type)
    if city:
        query = query.filter(Post.city == city)
    if min_price is not None:
        query = query.filter(Post.price >= min_price)
    if max_price is not None:
        query = query.filter(Post.price <= max_price)
    return query.offset(offset).limit(limit).all()


def get_post(db: Session, post_id):
    return db.get(Post, post_id)


def create_post(db: Session, *, post_type: str, title: str, description: str,
                owner_id, city: str | None = None, price: float | None = None,
                availability_date=None, room_type: str | None = None,
                job_category: str | None = None, travel_date=None,
                route: str | None = None):
    post = Post(
        post_type=post_type,
        title=title,
        description=description,
        owner_id=owner_id,
        city=city,
        price=price,
        availability_date=availability_date,
        room_type=room_type,
        job_category=job_category,
        travel_date=travel_date,
        route=route,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def update_post(db: Session, post: Post, **fields):
    for key, value in fields.items():
        if value is not None:
            setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post: Post):
    db.delete(post)
    db.commit()
