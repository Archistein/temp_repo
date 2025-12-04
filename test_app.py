import math
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_calc():
    response = client.post("/api/v1/calc", params={'a': 1, 'op': '+', 'b': 2})
    assert response.status_code == 200
    assert response.json() == 3

    response = client.post("/api/v1/calc", params={'a': 8.7, 'op': '-', 'b': 3.4})
    assert response.status_code == 200
    assert math.isclose(response.json(), 5.3)

    response = client.post("/api/v1/calc", params={'a': 7, 'op': '*', 'b': 7})
    assert response.status_code == 200
    assert response.json() == 49

    response = client.post("/api/v1/calc", params={'a': 5, 'op': '/', 'b': 2})
    assert response.status_code == 200
    assert response.json() == 2.5