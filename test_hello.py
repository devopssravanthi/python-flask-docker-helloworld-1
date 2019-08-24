# test_hello.py
from hello import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 2001
    assert response.data == b'Hello World!'
