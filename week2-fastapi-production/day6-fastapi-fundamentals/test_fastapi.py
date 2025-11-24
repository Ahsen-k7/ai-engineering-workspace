from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes", json={"title": "Testing", "content": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Testing"

def test_read_all_notes():
    response = client.get("/notes")
    assert response.status_code == 200

def test_update_note():
    # create first
    create_res = client.post("/notes", json={"title": "Old", "content": "Old content"})
    note_id = create_res.json()["id"]

    # update
    update_res = client.put(f"/notes/{note_id}", json={"title": "New"})
    assert update_res.status_code == 200
    assert update_res.json()["title"] == "New"

def test_delete_note():
    res = client.post("/notes", json={"title": "Delete Me", "content": "Bye"})
    note_id = res.json()["id"]

    delete_res = client.delete(f"/notes/{note_id}")
    assert delete_res.status_code == 200
