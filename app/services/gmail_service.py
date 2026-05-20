import requests


def fetch_filtered_emails(token: str):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages",
        headers=headers,
        params={"maxResults": 10}
    )

    email_data = response.json()

    messages = email_data.get("messages", [])

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

        snippet = data.get("snippet", "")

        email_text = f"{subject} {snippet}".lower()

        is_potential = any(
            keyword in email_text
            for keyword in keywords
        )

        if is_potential:

            results.append({
                "id": msg_id,
                "subject": subject,
                "sender": sender,
                "snippet": snippet
            })

    return results