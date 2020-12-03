from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from notebook.models import NoteBook
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_get_notebook_list_with_correct_jwt(client, create_token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {create_token}")
    url = reverse("notebook_list_url")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_notebook_with_correct_jwt(client, create_token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {create_token}")
    url = reverse("notebook_list_url")
    response = client.post(url, {"title": "test_notebook"}, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_notebook_list_with_random_jwt(client):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {'123'}")
    url = reverse("notebook_list_url")
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_post_notebook_with_radnom_jwt(client):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {'123'}")
    url = reverse("notebook_list_url")
    response = client.post(url, {"title": "test_notebook"}, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_notebook_list_with_no_jwt(client):
    url = reverse("notebook_list_url")
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_post_notebook_with_no_jwt(client):
    url = reverse("notebook_list_url")
    response = client.post(url, {"title": "test_notebook"}, format="json")
    assert response.status_code == 401
