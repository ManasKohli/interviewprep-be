from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_google_id(
    db: Session,
    google_id: str
):
    return (
        db.query(User)
        .filter(User.google_id == google_id)
        .first()
    )

def create_user(
        db: Session,
        email: str,
        google_id: str,
        name: str
):
    user = User(
        email=email,
        google_id=google_id,
        name=name
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_or_create_user(
        db: Session,
        email: str,
        google_id: str,
        name: str
):
    user = get_user_by_google_id(db, google_id)
    if user:
        return user

    return create_user(db, email, google_id, name)