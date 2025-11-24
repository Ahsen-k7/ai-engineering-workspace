from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root_injects_settings(monkeypatch):
    monkeypatch.setenv("ADMIN_EMAIL", "test@admin.com")
    monkeypatch.setenv("DEBUG", "True")
    response = client.get("/")
    data = response.json()
    assert data["admin"] == "test@admin.com"
    assert data["debug_mode"] is True