from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from notebook.models import NoteBook
from django.contrib.auth.models import User


@pytest.fixture()
def notebook():
    notebook = NoteBook.objects.create(title="test_check_notebook")
    return notebook


@pytest.mark.django_db
def test_get_detail_notebook_with_correct_jwt(client, create_token, notebook):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {create_token}")
    url = reverse("notebook_detail_url", kwargs={"pk": notebook.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == {"id": notebook.pk, "title": "test_check_notebook"}


@pytest.mark.django_db
def test_put_notebook_with_correct_jwt(client, create_token, notebook):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {create_token}")
    url = reverse("notebook_detail_url", kwargs={"pk": notebook.pk})
    response = client.put(url, {"title": "new title from put"}, format="json")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_notebook_with_correct_jwt(client, create_token, notebook):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {create_token}")
    url = reverse("notebook_detail_url", kwargs={"pk": notebook.pk})
    response = client.delete(url)
    assert response.status_code == 204
    