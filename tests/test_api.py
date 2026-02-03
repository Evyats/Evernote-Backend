from re import A
from fastapi.testclient import TestClient
from src.app import app, some_function
from src.core.logging import logger


client = TestClient(app)



def test_general():
    r = client.get("/health")
    print(r)
    a = some_function()
    assert 5 == a



def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "healthy"}



def test_get_user():
    response = client.get("/api/users")
    print(response)
    assert True