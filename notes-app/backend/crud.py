from sqlalchemy.orm import Session
from . import models, schemas

def list_notes(db: Session):
    return db.query(models.Note).order_by(models.Note.created_at.desc()).all()

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def create_note(db: Session, payload: schemas.NoteCreate):
    note = models.Note(title=payload.title, content=payload.content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def update_note(db: Session, note_id: int, payload: schemas.NoteUpdate):
    note = get_note(db, note_id)
    if not note:
        return None
    if payload.title is not None:
        note.title = payload.title
    if payload.content is not None:
        note.content = payload.content
    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: int):
    note = get_note(db, note_id)
    if not note:
        return False
    db.delete(note)
    db.commit()
    return True
