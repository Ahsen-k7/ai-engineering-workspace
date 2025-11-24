from database import notes_db, next_id
from models import Note, NoteCreate, NoteUpdate

def create_note(data: NoteCreate) -> Note:
    global next_id
    note = Note(id=next_id, title=data.title, content=data.content)
    notes_db.append(note)
    next_id += 1
    return note

def get_all_notes() -> list[Note]:
    return notes_db

def get_note(note_id: int) -> Note | None:
    for note in notes_db:
        if note.id == note_id:
            return note
    return None

def update_note(note_id: int, data: NoteUpdate) -> Note | None:
    note = get_note(note_id)
    if not note:
        return None
    
    if data.title is not None:
        note.title = data.title
    if data.content is not None:
        note.content = data.content
    
    return note

def delete_note(note_id: int) -> bool:
    global notes_db
    original_length = len(notes_db)
    notes_db = [note for note in notes_db if note.id != note_id]
    return len(notes_db) < original_length
