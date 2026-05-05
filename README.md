# InterviewPrep AI 🚀

A full-stack AI-powered tool that scans your Gmail inbox for interview invitations and automatically generates personalized interview prep.

---

## 🧠 Overview

InterviewPrep AI helps users streamline their interview process by:

* 📩 Detecting interview-related emails from Gmail
* 🧠 Extracting key details using AI
* 📊 Organizing interviews in a dashboard
* 🎯 Generating tailored interview preparation material

---

## 🏗️ Tech Stack

### Backend

* FastAPI (Python)
* PostgreSQL (coming soon)
* Gmail API
* OpenAI API

### Frontend (coming soon)

* React

---

## ⚙️ Features (MVP)

* Google OAuth login
* Fetch emails from Gmail
* Filter interview-related emails
* Extract structured interview data (company, role, date, type)
* Generate interview prep using AI

---

## 📁 Project Structure

```
interview-prep-backend/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── config.py           # Environment/config management
│   │
│   ├── routes/             # API endpoints
│   │   └── auth.py
│   │
│   ├── services/           # Business logic
│   │   └── google_auth_service.py
│   │
│   ├── models/             # Data models
│   │   └── user.py
│   │
│   └── db/                 # Database setup
│       └── database.py
│
├── run.py                  # Server entry point
├── requirements.txt
├── .env
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repo

```
git clone https://github.com/yourusername/interview-prep-ai.git
cd interview-prep-backend
```

---

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:8000/auth/callback
```

---

### 5. Run the backend

```
python run.py
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🔐 Google OAuth Setup

1. Go to Google Cloud Console
2. Create a new project
3. Enable Gmail API
4. Configure OAuth consent screen
5. Create OAuth Client ID
6. Add redirect URI:

```
http://localhost:8000/auth/callback
```

---

## 📌 API Endpoints (Current)

* `GET /` → health check
* `GET /auth/google` → start Google login
* `GET /auth/callback` → OAuth callback

---

## 🧪 Development Notes

* Uses Gmail API to fetch emails
* Uses OpenAI to extract structured interview data
* Focused on MVP simplicity over full automation

---

## 🚀 Roadmap

* [ ] Store interviews in PostgreSQL
* [ ] React dashboard UI
* [ ] AI-generated prep content
* [ ] Better email parsing

---

## 💡 Inspiration

This project was built to:

* Learn full-stack development
* Work with real-world APIs
* Build a practical AI-powered tool

---

## ⚠️ Disclaimer

This project is for educational purposes and is not production-ready.

---

## 👤 Author

Manas Kohli
