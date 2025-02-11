import pytest 
from app import app
#from <file or module> import <object or class>

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greetme(client):
    response = client.get('/')
    assert response.data==b'Welcome to flask home JR!'
    assert response.status_code==200

def test_page(client):
    response = client.get('/page1')
    assert response.data==b'Welcome to flask page1 JR!'
    assert response.status_code==200