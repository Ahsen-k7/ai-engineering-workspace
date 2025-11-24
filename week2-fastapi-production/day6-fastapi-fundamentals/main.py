from fastapi import FastAPI, HTTPException
from models import NoteCreate, NoteUpdate, Note
import crud

app = FastAPI(title="Day 6 - Notes CRUD API")

@app.post("/notes", response_model=Note)
def create(data: NoteCreate):
    return crud.create_note(data)

@app.get("/notes", response_model=list[Note])
def read_all():
    return crud.get_all_notes()

@app.get("/notes/{note_id}", response_model=Note)
def read_one(note_id: int):
    note = crud.get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/notes/{note_id}", response_model=Note)
def update(note_id: int, data: NoteUpdate):
    note = crud.update_note(note_id, data)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.delete("/notes/{note_id}")
def delete(note_id: int):
    deleted = crud.delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Deleted"}
