from django.urls import reverse
import pytest
from notebook.models import NoteBook


@pytest.fixture()
def notebook(user):
    notebook = NoteBook.objects.create(title="test_check_notebook", author=user)
    return notebook


# @pytest.mark.django_db
# def test_get_note_detail_
