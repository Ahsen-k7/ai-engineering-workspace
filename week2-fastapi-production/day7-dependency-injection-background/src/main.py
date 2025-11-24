from fastapi import FastAPI, Depends, BackgroundTasks, UploadFile, File
from src.config import get_settings, Settings
from src.tasks import send_welcome_email, process_uploaded_file
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Week 2 Day 2 – DI + Background + Upload",
    description="Production patterns by Ahsen & Hamza",
    version="0.1.0"
)

class UserCreate(BaseModel):
    name: str
    email: EmailStr

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Day 2 LIVE",
        "app": settings.app_name,
        "admin": settings.admin_email,
        "debug_mode": settings.debug
    }

@app.post("/register/")
async def register(
    user: UserCreate,
    background: BackgroundTasks,
    settings: Settings = Depends(get_settings)
):
    background.add_task(send_welcome_email, user.email, user.name)
    return {"message": f"{user.name} registered! Welcome email sending in background..."}

@app.post("/upload/")
async def upload_file(
    background: BackgroundTasks,
    file: UploadFile = File(...)
):
    # Simulate file size
    size_mb = 45.7
    background.add_task(process_uploaded_file, file.filename, size_mb)
    return {"message": f"{file.filename} accepted → processing started in background!"}