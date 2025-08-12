from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import main
from app.database import Base, get_db
import os

# Use an in-memory SQLite DB for fast unit tests
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# override dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

main.app.dependency_overrides[get_db] = override_get_db

Base.metadata.create_all(bind=engine)
client = TestClient(main.app)

def test_create_user():
    response = client.post("/users/", json={"email":"hello@example.com", "password":"secret"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "hello@example.com"
    assert "id" in data

def test_create_item_for_user():
    # create user
    res = client.post("/users/", json={"email":"user2@example.com", "password":"pwd"})
    uid = res.json()["id"]
    res2 = client.post(f"/users/{uid}/items/", json={"title":"My item", "description":"desc"})
    assert res2.status_code == 200
    assert res2.json()["title"] == "My item"
