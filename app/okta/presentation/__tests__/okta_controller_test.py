import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_list_users(client):
    resp = client.get("/okta/list_users")

    assert resp.status_code == 200

    data = resp.get_json()
    len(data) > 0
