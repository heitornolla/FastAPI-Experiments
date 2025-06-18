from http import HTTPStatus


def test_root_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
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
        'id': 1,
    }


# Dependent test is a code smell
def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'test', 'email': 'test@example.com'}]
    }


def test_update_user(client):
    response = client.put(
        url='/users/1/',
        json={
            'username': 'updated',
            'email': 'new_email@example.com',
            'password': 'new_password',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'updated',
        'email': 'new_email@example.com',
        'id': 1,
    }


def test_update_invalid_user(client):
    response = client.put(
        url='/users/-1/',
        json={
            'username': 'updated',
            'email': 'new_email@example.com',
            'password': 'new_password',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
