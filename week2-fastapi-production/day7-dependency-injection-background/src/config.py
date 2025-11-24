# backend/src/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path

# This points to the workspace root (two levels up from backend/src)
ROOT_DIR = Path(__file__).parent.parent.parent.parent   # workspace root
ENV_PATH = ROOT_DIR / ".env"

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    admin_email: str
    debug: bool = False
    items_per_user: int = 50

    model_config = {
        "env_file": str(ENV_PATH),      # ← reads from root .env
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }

@lru_cache
def get_settings() -> Settings:
    return Settings()