from fastapi import APIRouter
from app.services.gmail_service import fetch_filtered_emails
from app.services.ai_service import analyze_email_content

router = APIRouter(prefix="/gmail")

@router.get("/emails")
def get_emails(token: str):
    emails = fetch_filtered_emails(token)
    results = []

    for email in emails:

        analysis = analyze_email_content(email["subject"], email["snippet"])
        results.append({'email': email, 'analysis': analysis})
        
    return {"emails": results}
