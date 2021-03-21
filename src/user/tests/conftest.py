from user.models import User
import pytest


@pytest.fixture()
def user():
    user = User.objects.create_superuser(
        username="testuser", 
        email="test@mail.com",
        password="testpassword",
    )
    return user
