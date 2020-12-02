import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_jwt_token_create_user_in_db(user):
    client = APIClient()
    url = reverse("token_obtain_pair")
    response = client.post(url, {
        "username": "testuser",
        "password": "testpassword",
    })
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_jwt_token_create_user_not_in_db():
    client = APIClient()
    url = reverse("token_obtain_pair")
    response = client.post(url, {
        "username": "testuser",
        "password": "testpassword",
    })
    assert response.status_code == 401
