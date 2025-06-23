from http import HTTPStatus

from fastapi_project.schemas import UserPublic


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


def test_read_users_no_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
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


def test_delete_user(client, user):
    response = client.delete(url='/users/1/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_invalid_user(client):
    response = client.delete(
        url='/users/-1/',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_integrity_error(client, user):
    # Criando um registro para "bob"
    client.post(
        '/users',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    # Alterando o user.username das fixture para bob
    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'bob',
            'email': 'email@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {'detail': 'Username or Email already exists'}


def test_get_token(client, user):
    response = client.post(
        '/token/', data={'username': user.email, 'password': user.clean_password}
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token
