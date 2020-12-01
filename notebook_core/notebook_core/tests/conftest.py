from django.contrib.auth.models import User
import pytest


@pytest.fixture()
def create_user():
    user = User.objects.create_superuser(
        username="testuser", 
        email="test@mail.com",
        password="testpassword"
    )
    return user