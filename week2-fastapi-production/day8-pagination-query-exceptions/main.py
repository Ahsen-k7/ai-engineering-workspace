from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List, Optional
import logging
from src.models import Note
from src.database import notes_db

# ────── Structured Logging Setup (Production Style) ──────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("notes-api")
# ─────────────────────────────────────────────────────────────

app = FastAPI(title="Week 2 Day 8 – Notes API + Logging + Pagination")

# Custom exception handler
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    logger.error(f"Bad Request → {str(exc)} | path={request.url.path} | query_params={request.query_params}")
    return JSONResponse(status_code=400, content={"detail": str(exc)})

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTP {exc.status_code} → {exc.detail} | path={request.url.path}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.get("/notes/", response_model=List[Note])
async def get_notes(
    skip: int = Query(0, ge=0, description="Skip first N notes"),
    limit: int = Query(10, ge=1, le=100, description="Max notes to return"),
    search: Optional[str] = Query(None, description="Search in title or content"),
    tag: Optional[str] = Query(None, alias="category", description="Filter by tag")
):
    logger.info(f"GET /notes | skip={skip} limit={limit} search='{search}' category='{tag}'")

    filtered = notes_db

    if search:
        search_lower = search.lower()
        filtered = [
            note for note in filtered
            if search_lower in note.title.lower() or search_lower in note.content.lower()
        ]
        logger.info(f"Search applied → {len(filtered)} notes match")

    if tag:
        tag_lower = tag.lower()
        filtered = [note for note in filtered if tag_lower in note.title.lower()]
        logger.info(f"Category filter applied → {len(filtered)} notes remain")

    total = len(filtered)

    if skip >= total and total > 0:
        raise ValueError(f"skip={skip} is too high. Only {total} notes match your filters.")

    result = filtered[skip:skip + limit]
    logger.info(f"Returning {len(result)} notes (skip={skip}, limit={limit})")

    return result

@app.get("/notes/{note_id}", response_model=Note)
async def get_note(note_id: int):
    logger.info(f"GET /notes/{note_id}")
    note = next((n for n in notes_db if n.id == note_id), None)
    if not note:
        logger.warning(f"Note {note_id} not found")
        raise HTTPException(status_code=404, detail="Note not found")
    return note