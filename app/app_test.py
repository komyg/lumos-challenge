import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_capabilities(client):
    resp = client.get("/capabilities/okta")
    print(resp.data)
    assert resp.data == b"Not implemented!"

def test_read(client):
    resp = client.get("/okta/list_users")
    assert resp.data == b"Some result from the list_users operation on app okta"

def test_mutate(client):
    resp = client.post("/okta/suspend_user", json={"test": "body"})
    assert resp.data == b"Some result from the mutation operation suspend_user on app okta - did it work?"
