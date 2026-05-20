import os
from dotenv import load_dotenv
from openai import OpenAI

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

