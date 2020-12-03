from user.models import User
from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.fixture()
def client():
    client = APIClient()
    return client


@pytest.fixture()
def create_token(client):
    user = User.objects.create_superuser(
        username="testuser", 
        email="test@mail.com",
        password="testpassword"
    )
    url = reverse("token_obtain_pair")
    response = client.post(url, {
        "username": "testuser",
        "password": "testpassword",
    })
    return response.data["access"]
