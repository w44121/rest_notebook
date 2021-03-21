from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from user.models import User
from notebook.models import NoteBook


@pytest.fixture()
def client():
    client = APIClient()
    return client


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
    return response.data["access"]

@pytest.fixture()
def notebook(user):
    notebook = NoteBook.objects.create(title="test_check_notebook", author=user)
    return notebook
