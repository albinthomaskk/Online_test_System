from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/auth/register", json={"username": "testuser", "password": "testpass", "role": "user"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login():
    response = client.post("/auth/login", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()
