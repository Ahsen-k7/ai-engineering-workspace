from datetime import datetime
from models import Note

notes_db = [
    Note(
        id=i,
        title=f"Note {i} - {'Important' if i % 5 == 0 else 'Regular'} {'HOMEWORK' if i % 7 == 0 else ''}".strip(),
        content=f"This is the content of note number {i}. Let's test search and filtering. {'Homework due tomorrow!' if i % 11 == 0 else ''}",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    for i in range(1, 101)
]