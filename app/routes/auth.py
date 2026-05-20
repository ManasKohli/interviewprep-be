from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.services.google_auth_service import handle_google_callback, login_with_google

router = APIRouter(prefix="/auth")


@router.get("/login")
def google_login():
    auth_url = login_with_google()
    return RedirectResponse(auth_url)

@router.get("/callback")
def google_callback(code: str):
    data = handle_google_callback(code)
    return {"access_token": data[0], "user_info": data[1]}

