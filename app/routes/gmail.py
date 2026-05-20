from fastapi import APIRouter
from app.services.gmail_service import get_emails as fetch_emails

router = APIRouter(prefix="/gmail")

@router.get("/emails")
def get_emails(token: str):
    results = fetch_emails(token)
    return {"emails": results}
