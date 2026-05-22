import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_email_content(subject, snp):

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
    results = response.choices[0].message.content
    print(results)
    return results

def generate_interview_prep(company, role):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You generate interview preparation material
                for software engineering interviews.

                Return ONLY valid JSON.
                """
            },
            {
                "role": "user",
                "content": f"""
                Company: {company}

                Role: {role}

                Generate:
                - 5 important interview topics
                - 5 technical interview questions
                """
            }
        ]
    )

    content = response.choices[0].message.content
    return json.loads(content)