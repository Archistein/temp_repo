import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    response = client.post("/api/v1/calc", params={'a': 1, 'op': '+', 'b': 2})
    assert response.status_code == 200
    assert response.json() == 3