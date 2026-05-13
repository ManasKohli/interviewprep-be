from fastapi import APIRouter
import requests

router = APIRouter(prefix="/gmail")

@router.get("/emails")
def get_emails(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
         "https://gmail.googleapis.com/gmail/v1/users/me/messages",
        headers=headers,
        params={"maxResults": 10}
    )

    email_data = response.json()
    return email_data