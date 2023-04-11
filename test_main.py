import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "http://localhost/" or response.location  == "/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_links(client):
    response = client.get("/links")
    assert response.status_code == 200
    assert b"<title>Useful links</title>" in response.data

def test_sh(client):
    response = client.get("/sh")
    assert response.status_code == 200
    assert b"<title>How to: sh</title>" in response.data


