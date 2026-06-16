from fastapi import APIRouter
from app.services.ai_service import analyze_email_content, generate_interview_prep

router = APIRouter(prefix="/ai", tags=["AI"])

#test endpoint
@router.get("/test")
def test_ai():
    # hardcoded data
    material = generate_interview_prep("Google", "Software Engineer I")

    return {
        "material": material
    }