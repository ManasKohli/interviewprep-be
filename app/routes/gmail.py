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
    messages = email_data.get("messages", [])

    results = []
    for msg in messages:
        msg_id = msg["id"]
        msg_response = requests.get(
            f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{msg_id}",
              headers=headers
        )
        data = msg_response.json()

        payload = data.get("payload", {})
        headers_list = payload.get("headers", [])

        subject = ""
        sender = ""

        for header in headers_list:
            if header["name"] == "Subject":
                subject = header["value"]
            elif header["name"] == "From":
                sender = header["value"]
        
        snp = data.get("snippet", "")
        keywords = [
        "interview",
        "recruiter",
        "assessment",
        "screening",
        "technical",
        "coding challenge",
        "software engineer",
        "intern"
        ]
        email_text = f"{subject} {snp}".lower()
        is_potential = any(keyword in email_text for keyword in keywords)
        if is_potential:
            results.append({"id": msg_id, "snippet": snp, "subject": subject, "sender": sender})
            
    return {'emails': results}