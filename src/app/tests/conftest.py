from django.urls import reverse
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


@pytest.fixture()
def token(client, user):
    url = reverse("token_obtain_pair")
    response = client.post(url, {
        "username": "testuser",
        "password": "testpassword",
    })
    return (
        response.data["access"],
        response.data["refresh"],
    )
