from app.db.session import SessionLocal
from app.services.user_service import get_user_by_google_id

db = SessionLocal()

user = get_user_by_google_id(db=db, google_id="1234567890")
print(user.email)
db.close()
