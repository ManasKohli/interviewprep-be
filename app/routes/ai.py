from fastapi import APIRouter
from app.services.ai_service import analyze_email_content

router = APIRouter(prefix="/ai")

@router.get("/analyze")
def analyze_email():
    #hardcoded email
    subject = "tech email"
    snp = "we would like to invite you to interview for a swe role at aws"

    analysis = analyze_email_content(subject, snp)
    return {"analysis": analysis}