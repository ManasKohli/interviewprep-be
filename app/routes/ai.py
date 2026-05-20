import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import APIRouter
import requests

load_dotenv()
router = APIRouter(prefix="/ai")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@router.get("/analyze")
def analyze_email():
    #hardcoded email
    subject = "tech email"
    snp = "we would like to invite you to interview for a swe role at aws"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You analyze recruiting emails.

                Determine:
                - Is this a technical interview email?
                - Company name
                - Role
                - Interview stage

                Return ONLY valid JSON.
                """
            },
            {
                "role": "user",
                "content": f"""
                Subject: {subject}

                Snippet:
                {snp}
                """
            }
        ]
    )
    print(response.choices[0].message.content)
    return {
    "response": response.choices[0].message.content
}
