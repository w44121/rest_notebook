from django.urls import reverse
from rest_framework.exceptions import ErrorDetail
import pytest


@pytest.mark.django_db
def test_get_notebook_list_with_correct_jwt(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("notebook_list_url")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_notebook_with_correct_jwt(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("notebook_list_url")
    response = client.post(url, {"title": "test_notebook"}, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_6_notebook_with_correct_jwt_no_premium_user(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("notebook_list_url")
    for _ in range(6):
        response = client.post(url, {"title": "test_notebook"}, format="json")
    # dont work
    assert response.data["error"] == [ErrorDetail(string='only premium users can have more then 5 notebooks', code='invalid')]


@pytest.mark.django_dbs
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
