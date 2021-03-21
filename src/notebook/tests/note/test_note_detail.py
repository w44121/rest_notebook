from django.urls import reverse
import pytest
from notebook.models import Note


@pytest.fixture()
def note(notebook):
    note = Note.objects.create(text="test text for test note", notebook=notebook)
    return note


@pytest.fixture()
def client_with_access(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client


@pytest.mark.django_db
def test_get_note_detail(client_with_access, note):
    url = reverse("note_detail_url", kwargs={"pk": note.pk})
    response = client_with_access.get(url)
    assert response.data["text"] == "test text for test note"
    assert response.status_code == 200


@pytest.mark.django_db
def test_put_note_datail(client_with_access, note, notebook):
    url = reverse("note_detail_url", kwargs={"pk": note.pk})
    response = client_with_access.put(url, {"text": "updated note text", "notebook": notebook.pk}, format="json")
    assert response.data["text"] == "updated note text"
    assert response.status_code == 200


@pytest.mark.django_db
def test_del_note_detail(client_with_access, note):
    url = reverse("note_detail_url", kwargs={"pk": note.pk})
    response = client_with_access.delete(url)
    assert response.status_code == 204
