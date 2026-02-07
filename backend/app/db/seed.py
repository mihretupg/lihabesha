from datetime import datetime, timedelta, timezone
from app.db.session import SessionLocal
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app.models.message import Message
from app.models.report import Report
from app.models.moderation_action import ModerationAction  # noqa: F401
from app.core.security import hash_password


def seed():
    db = SessionLocal()
    try:
        # Users
        demo_users = [
            {
                "email": "admin@lihabesha.local",
                "name": "Admin User",
                "city": "Addis Ababa",
                "language": "am",
                "role": "admin",
                "password": "AdminPass123!",
            },
            {
                "email": "moderator@lihabesha.local",
                "name": "Moderator User",
                "city": "Asmara",
                "language": "ti",
                "role": "moderator",
                "password": "ModPass123!",
            },
            {
                "email": "user1@lihabesha.local",
                "name": "Selam Gebre",
                "city": "Washington, DC",
                "language": "am",
                "role": "user",
                "password": "UserPass123!",
            },
            {
                "email": "user2@lihabesha.local",
                "name": "Dawit Tesfay",
                "city": "Seattle, WA",
                "language": "ti",
                "role": "user",
                "password": "UserPass123!",
            },
        ]

        users = {}
        for data in demo_users:
            existing = db.query(User).filter(User.email == data["email"]).first()
            if existing:
                users[data["email"]] = existing
                continue
            user = User(
                email=data["email"],
                name=data["name"],
                city=data["city"],
                language=data["language"],
                role=data["role"],
                password_hash=hash_password(data["password"]),
                is_active=True,
            )
            db.add(user)
            db.flush()
            users[data["email"]] = user

        db.commit()

        # Posts
        def ensure_post(title: str):
            return db.query(Post).filter(Post.title == title).first()

        now = datetime.now(timezone.utc)

        posts_data = [
            {
                "title": "Room available near U Street",
                "description": "Private room in a 3BR. Utilities included. Quiet neighborhood.",
                "post_type": "housing",
                "city": "Washington, DC",
                "price": 850,
                "availability_date": now + timedelta(days=14),
                "room_type": "Private",
                "owner_email": "user1@lihabesha.local",
            },
            {
                "title": "Hiring: Cafe barista",
                "description": "Part-time barista needed. Weekend shifts. Experience preferred.",
                "post_type": "job",
                "city": "Seattle, WA",
                "price": None,
                "job_category": "hospitality",
                "owner_email": "user2@lihabesha.local",
            },
            {
                "title": "Traveling to Addis in March",
                "description": "Flying from IAD to ADD. Can carry small luggage.",
                "post_type": "travel",
                "city": "Washington, DC",
                "price": None,
                "travel_date": now + timedelta(days=30),
                "route": "IAD ? ADD",
                "owner_email": "user1@lihabesha.local",
            },
        ]

        created_posts = []
        for pdata in posts_data:
            existing = ensure_post(pdata["title"])
            if existing:
                created_posts.append(existing)
                continue
            post = Post(
                title=pdata["title"],
                description=pdata["description"],
                post_type=pdata["post_type"],
                city=pdata.get("city"),
                price=pdata.get("price"),
                availability_date=pdata.get("availability_date"),
                room_type=pdata.get("room_type"),
                job_category=pdata.get("job_category"),
                travel_date=pdata.get("travel_date"),
                route=pdata.get("route"),
                owner_id=users[pdata["owner_email"]].id,
            )
            db.add(post)
            db.flush()
            created_posts.append(post)

        db.commit()

        # Comments
        if created_posts:
            first_post = created_posts[0]
            comment_exists = db.query(Comment).filter(Comment.post_id == first_post.id).first()
            if not comment_exists:
                comment = Comment(
                    post_id=first_post.id,
                    user_id=users["user2@lihabesha.local"].id,
                    body="Is this still available? I can move in next month.",
                )
                db.add(comment)
                db.commit()

        # Messages
        msg_exists = db.query(Message).filter(Message.body.ilike("%Hello%")) .first()
        if not msg_exists:
            message = Message(
                from_user_id=users["user1@lihabesha.local"].id,
                to_user_id=users["user2@lihabesha.local"].id,
                body="Hello! Let me know if you're interested in the room.",
            )
            db.add(message)
            db.commit()

        # Reports
        report_exists = db.query(Report).filter(Report.reason.ilike("%spam%")) .first()
        if not report_exists and created_posts:
            report = Report(
                post_id=created_posts[-1].id,
                reporter_id=users["moderator@lihabesha.local"].id,
                reason="Looks like possible spam, needs review.",
            )
            db.add(report)
            db.commit()

        print("seeded")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
