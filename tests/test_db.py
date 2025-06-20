from fastapi_project.models import User


def test_create_user(session):
    user = User(username='test', email='test@example.com', password='secret')

    session.add(user)
    session.commit()

    assert user.username == 'test'
    assert user.email == 'test@example.com'
    assert user.password == 'secret'
