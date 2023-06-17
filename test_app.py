from app import app
import pytest
import requests


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World' in response.data

def test_values(client):
    response = client.get('/?value1=Hello&value2=World')
    assert response.status_code == 200
    assert b'value1=Hello' in response.data
    assert b'value2=World' in response.data

def test_no_values(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'value1=No Value Provided' in response.data
    assert b'value2=No Value Provided' in response.data

