from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pathlib import Path
from typing import List

from .db import Base, engine, get_db
from . import crud, schemas, models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/api/notes", response_model=List[schemas.NoteOut])
def list_(db: Session = Depends(get_db)):
    return crud.list_notes(db)

@app.post("/api/notes", response_model=schemas.NoteOut, status_code=201)
def create(payload: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, payload)

@app.put("/api/notes/{note_id}", response_model=schemas.NoteOut)
def update(note_id: int, payload: schemas.NoteUpdate, db: Session = Depends(get_db)):
    note = crud.update_note(db, note_id, payload)
    if not note:
        raise HTTPException(404, "Not found")
    return note

@app.delete("/api/notes/{note_id}", status_code=204)
def delete(note_id: int, db: Session = Depends(get_db)):
    if not crud.delete_note(db, note_id):
        raise HTTPException(404, "Not found")
    return

# Serve frontend if built
FRONTEND_DIR = Path(__file__).parent.parent / "frontend_dist"
if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
