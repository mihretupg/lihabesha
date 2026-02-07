# Lihabesha Community Platform

Habesha Community Platform for housing, jobs, travel notices, and community interaction.

## Tech Stack
- Frontend: Vite + React + Tailwind CSS
- Backend: Python (FastAPI)
- Database: PostgreSQL
- Auth: JWT

## Repo Structure
- `backend/` FastAPI API, business logic, DB models
- `frontend/` Vite + React app
- `docs/` Project docs, SRS notes

## Backend (FastAPI)
- `backend/app/main.py`

Run locally:
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend (Vite + React + Tailwind)
```bash
cd frontend
npm install
npm run dev
```

## Next Steps
- Define DB models for User, Post, Message, Comment, Report
- Build auth (JWT), listing CRUD, filters, and messaging
- Add moderation endpoints and basic admin tooling
