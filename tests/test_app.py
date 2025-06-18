from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_project.app import app


def test_root_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'test@example.com',
            'password': 'secretpassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'test',
        'email': 'test@example.com',
    }
