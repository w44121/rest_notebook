from django.urls import reverse
import pytest
from notebook.models import NoteBook


@pytest.fixture()
def notebook(user):
    notebook = NoteBook.objects.create(title="test_check_notebook", author=user)
    return notebook


@pytest.mark.django_db
def test_get_note_list_from_correct_notebook_with_correct_jwt(client, token, notebook):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("note_list_url", kwargs={"pk": notebook.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_post_note_on_correct_notebook_with_correct_jwt(client, token, notebook):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("note_list_url", kwargs={"pk": notebook.id})
    response = client.post(url, {"text": "test note text 1", "notebook": notebook.id}, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_note_list_from_field_notebook_with_correct_jwt(client, token, notebook):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("note_list_url", kwargs={"pk": 10})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_note_list_from_correct_notebook_with_random_jwt(client, token, notebook):
    client.credentials(HTTP_AUTHORIZATION="Bearer 123")
    url = reverse("note_list_url", kwargs={"pk": notebook.id})
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_post_note_on_correct_notebook_with_random_jwt(client, token, notebook):
    client.credentials(HTTP_AUTHORIZATION="Bearer 123")
    url = reverse("note_list_url", kwargs={"pk": notebook.id})
    response = client.post(url, {"text": "test note text 1", "notebook": notebook.id}, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_note_list_from_correct_notebook_with_nnno_jwt(client, notebook):
    url = reverse("note_list_url", kwargs={"pk": notebook.id})
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_post_note_on_correct_notebook_with_no_jwt(client, notebook):
    url = reverse("note_list_url", kwargs={"pk": notebook.id})
    response = client.post(url, {"text": "test note text 1", "notebook": notebook.id}, format="json")
    assert response.status_code == 401
