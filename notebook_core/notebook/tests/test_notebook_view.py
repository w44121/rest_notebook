from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from notebook.models import NoteBook


@pytest.mark.django_db
def test_get_notebook_list():
    client = APIClient()
    url = reverse("notebook_list_url")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_notebook():
    client = APIClient()
    url = reverse("notebook_list_url")
    response = client.post(url, {"title": "test_notebook"}, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_detail_notebook():
    client = APIClient()
    notebook = NoteBook.objects.create(title="test_check_notebook")
    url = reverse("notebook_detail_url", kwargs={"pk": notebook.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == {"id": notebook.pk, "title": "test_check_notebook"}