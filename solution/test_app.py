import pytest
from flask import Flask
from app import app  # replace with the name of your flask app file without .py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_register(client):
    # Assuming that the user doesn't exist yet
    response = client.post('/registersuccess', data={
        'name': 'Nk',
        'email': 'nk@test.com',
        'password': 'passwordpk'
    })

    assert response.status_code == 200
    # Assuming that after successful registration, the user is redirected to the login page
    assert b'Please sign in' in response.data

def test_login(client):
    # Assuming that the user was registered successfully
    response = client.post('/loginsuccess', data={
        'email': 'pk@test.com',
        'password': 'passwordpk'
    })

    assert response.status_code == 200
    # Assuming that after successful login, the user is redirected to the dashboard page
    assert b'Welcome PK' in response.data
