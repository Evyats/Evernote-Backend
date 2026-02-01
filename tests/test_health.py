from fastapi.testclient import TestClient
from src.app import app, some_function


client = TestClient(app)


def test_hello():
    # app.health()
    r = client.get("/health")
    print(r)
    a = some_function()
    assert 5 == a