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
            {
                "email": "user3@lihabesha.local",
                "name": "Saba Lemma",
                "city": "Dallas, TX",
                "language": "am",
                "role": "user",
                "password": "UserPass123!",
            },
            {
                "email": "user4@lihabesha.local",
                "name": "Hagos Girmay",
                "city": "Minneapolis, MN",
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
                "title": "Basement studio in Silver Spring",
                "description": "Cozy studio, separate entrance. Looking for long-term tenant.",
                "post_type": "housing",
                "city": "Silver Spring, MD",
                "price": 1100,
                "availability_date": now + timedelta(days=7),
                "room_type": "Studio",
                "owner_email": "user3@lihabesha.local",
            },
            {
                "title": "Shared room in Minneapolis",
                "description": "Shared room in 2BR. Close to transit.",
                "post_type": "housing",
                "city": "Minneapolis, MN",
                "price": 650,
                "availability_date": now + timedelta(days=21),
                "room_type": "Shared",
                "owner_email": "user4@lihabesha.local",
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
                "title": "Dispatcher for trucking company",
                "description": "Full-time dispatcher role. Prior experience a plus.",
                "post_type": "job",
                "city": "Dallas, TX",
                "price": None,
                "job_category": "admin",
                "owner_email": "user3@lihabesha.local",
            },
            {
                "title": "Looking for nanny (weekends)",
                "description": "Weekend nanny needed. Flexible hours.",
                "post_type": "job",
                "city": "Washington, DC",
                "price": None,
                "job_category": "services",
                "owner_email": "user1@lihabesha.local",
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
            {
                "title": "Returning from Addis to JFK",
                "description": "Returning to NYC. Can bring documents or small items.",
                "post_type": "travel",
                "city": "New York, NY",
                "price": None,
                "travel_date": now + timedelta(days=45),
                "route": "ADD ? JFK",
                "owner_email": "user2@lihabesha.local",
            },
            {
                "title": "Boston to Asmara trip",
                "description": "Trip via Frankfurt. Limited luggage space.",
                "post_type": "travel",
                "city": "Boston, MA",
                "price": None,
                "travel_date": now + timedelta(days=60),
                "route": "BOS ? FRA ? ASM",
                "owner_email": "user4@lihabesha.local",
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
        comment_templates = [
            "Is this still available?",
            "What utilities are included?",
            "Can you share more photos?",
            "Is parking available?",
        ]
        for idx, post in enumerate(created_posts[:6]):
            existing = db.query(Comment).filter(Comment.post_id == post.id).first()
            if existing:
                continue
            commenter = users["user2@lihabesha.local"] if idx % 2 == 0 else users["user3@lihabesha.local"]
            comment = Comment(
                post_id=post.id,
                user_id=commenter.id,
                body=comment_templates[idx % len(comment_templates)],
            )
            db.add(comment)
        db.commit()

        # Messages
        message_pairs = [
            ("user1@lihabesha.local", "user2@lihabesha.local", "Hello! Let me know if you're interested."),
            ("user3@lihabesha.local", "user4@lihabesha.local", "Hi, are you still looking for a roommate?"),
            ("user2@lihabesha.local", "user1@lihabesha.local", "Thanks! Can we schedule a call?"),
        ]
        for from_email, to_email, body in message_pairs:
            exists = db.query(Message).filter(Message.body == body).first()
            if exists:
                continue
            msg = Message(
                from_user_id=users[from_email].id,
                to_user_id=users[to_email].id,
                body=body,
            )
            db.add(msg)
        db.commit()

        # Reports
        if created_posts:
            report_pairs = [
                (created_posts[0], "Possible duplicate listing."),
                (created_posts[-1], "Looks like spam, needs review."),
            ]
            for post, reason in report_pairs:
                exists = db.query(Report).filter(Report.post_id == post.id, Report.reason == reason).first()
                if exists:
                    continue
                report = Report(
                    post_id=post.id,
                    reporter_id=users["moderator@lihabesha.local"].id,
                    reason=reason,
                )
                db.add(report)
            db.commit()

        print("seeded")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
