# 📝 Notes App (React + FastAPI)

A minimal CRUD Notes App.

## Run locally

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
