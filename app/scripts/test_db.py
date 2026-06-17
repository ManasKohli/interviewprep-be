from app.db.session import SessionLocal
from app.models.user import User

db = SessionLocal()

user = User(
    email="test@example.com",
    google_id="1234567890",
    name="Test User",
)

db.add(user)
db.commit()
db.refresh(user)

print(user.id)
db.close()
