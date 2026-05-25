# InterviewPrep AI 🚀

> An AI-powered interview intelligence platform that automatically detects technical interview invitations from Gmail, extracts structured interview data using LLMs, generates personalized preparation plans, and schedules study sessions directly into Google Calendar.

---

# 📌 Overview

InterviewPrep AI is a full-stack SaaS application designed to automate the technical interview preparation workflow.

The platform connects to a user's Gmail account using Google OAuth, scans inbox activity for interview-related emails, uses Large Language Models to classify and extract interview metadata, and generates personalized preparation material tailored to the company, role, and interview stage.

The long-term vision is to build an intelligent interview copilot capable of:

* tracking interview pipelines
* generating adaptive study plans
* identifying company-specific interview patterns
* automating interview preparation workflows

---

# ✨ Core Features

## 🔐 Authentication & Authorization

* Google OAuth 2.0 authentication
* Secure Gmail API access
* Token management & refresh flow
* Session-based authentication (planned)

---

## 📩 Gmail Interview Detection

* Connect and scan Gmail inboxes
* Filter technical recruiting/interview emails
* Detect:

  * recruiter outreach
  * online assessments
  * technical interviews
  * behavioral interviews
  * onsite invitations

---

## 🧠 AI-Powered Interview Extraction

Uses OpenAI models to extract structured interview metadata:

```json
{
  "company": "Google",
  "role": "Software Engineer Intern",
  "stage": "Technical Interview",
  "date": "2026-06-01",
  "confidence": 0.94
}
```

Extracted information includes:

* Company
* Role
* Interview stage
* Interview date
* Confidence score
* Technical focus areas

---

## 🎯 Personalized Interview Preparation

Automatically generates:

* technical interview questions
* behavioral interview questions
* company-specific preparation advice
* study plans
* interview focus areas

---

## 📅 Smart Calendar Scheduling

Integrates with Google Calendar to:

* create prep sessions automatically
* schedule review blocks
* organize mock interviews
* manage interview timelines

---

# 🏗️ System Architecture

```text
User Login (Google OAuth)
            ↓
      Gmail API Access
            ↓
    Inbox Email Scanning
            ↓
   AI Interview Detection
            ↓
 Structured Metadata Extraction
            ↓
      PostgreSQL Storage
            ↓
 AI Prep Material Generation
            ↓
 Google Calendar Scheduling
            ↓
        Frontend Dashboard
```

---

# 🧰 Tech Stack

## Backend

* FastAPI
* Python
* SQLAlchemy
* Alembic
* PostgreSQL
* OpenAI API
* Gmail API
* Google Calendar API

---

## Frontend (In Progress)

* Next.js
* React
* TailwindCSS
* shadcn/ui

---

## Infrastructure & DevOps

* Docker
* Docker Compose
* Google Cloud Run
* Google Cloud SQL (PostgreSQL)
* Google Artifact Registry
* Google Secret Manager
* GitHub Actions (planned)

---

# 📂 Project Structure

```text
INTERVIEWPREP-BE/
│
├── app/
│   │
│   ├── main.py
│   ├── config.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── gmail.py
│   │   └── ai.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── gmail_service.py
│   │   └── google_auth_service.py
│   │
│   ├── models/
│   │
│   ├── db/
│   │
│   └── schemas/
│
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# ⚙️ Local Development Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/interviewprep-ai.git
cd INTERVIEWPREP-BE
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

REDIRECT_URI=http://localhost:8000/auth/callback

DATABASE_URL=postgresql://postgres:password@localhost/interviewprep
```

---

## 5. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server runs on:

```text
http://127.0.0.1:8000
```

---

# 🔐 Google OAuth Setup

## 1. Create Google Cloud Project

* Open Google Cloud Console
* Create a new project

---

## 2. Enable APIs

Enable:

* Gmail API
* Google Calendar API

---

## 3. Configure OAuth Consent Screen

* Add application name
* Add authorized domains
* Configure test users

---

## 4. Create OAuth Credentials

Create:

* OAuth Client ID
* Web Application

Authorized redirect URI:

```text
http://localhost:8000/auth/callback
```

---

# 📡 Current API Endpoints

## Authentication

```http
GET /auth/login
```

Redirects user to Google OAuth login.

---

```http
GET /auth/callback
```

Handles OAuth callback and returns user token data.

---

## Gmail

```http
GET /gmail/emails
```

Fetches and analyzes interview-related emails.

---

## AI

```http
GET /ai/test
```

Test endpoint for AI-generated interview preparation.

---

# 🧠 AI Workflow

```text
1. User connects Gmail
2. Backend scans inbox
3. Emails filtered for interview relevance
4. GPT classifies interview likelihood
5. Structured interview metadata extracted
6. Interview stored in PostgreSQL
7. AI generates personalized prep material
8. Calendar sessions scheduled automatically
```

---

# 🚀 Engineering Goals

This project is intentionally being built with production-oriented backend and infrastructure practices to deepen understanding of:

* backend architecture
* API design
* OAuth flows
* PostgreSQL database management
* Docker containerization
* cloud deployments
* DevOps workflows
* AI integrations
* scalable SaaS infrastructure

---

# 🛣️ Roadmap

## Backend

* [ ] SQLAlchemy models
* [ ] Alembic migrations
* [ ] JWT authentication
* [ ] Background task processing
* [ ] Async Gmail scanning
* [ ] AI prompt optimization
* [ ] Duplicate interview detection

---

## Frontend

* [ ] Next.js dashboard
* [ ] Interview tracking UI
* [ ] Authentication flow
* [ ] Calendar visualization
* [ ] AI prep viewer

---

## Infrastructure

* [ ] Docker containerization
* [ ] Docker Compose setup
* [ ] Cloud Run deployment
* [ ] Cloud SQL integration
* [ ] Secret Manager integration
* [ ] CI/CD pipeline

---

# 🎯 Long-Term Vision

InterviewPrep AI aims to evolve into an intelligent interview operating system capable of:

* tracking full recruiting pipelines
* generating adaptive preparation plans
* analyzing company-specific interview trends
* providing AI-powered interview coaching
* automating interview preparation workflows end-to-end

---

# ⚠️ Disclaimer

This project is currently under active development and is intended for educational and portfolio purposes.

---

# 👤 Author

**Manas Kohli**

Aspiring Software Engineer focused on:

* backend systems
* AI-powered applications
* cloud infrastructure
* DevOps engineering
