from fastapi_project.models import User


def test_create_user():
    user = User(username='test', email='test@example.com', password='secret')

    assert user.username == 'test'
    assert user.email == 'test@example'
    assert user.password == 'secret'
