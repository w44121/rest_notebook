from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_get_tags_list_with_correct_jwt(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("tag_list_url")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_tag_list_with_correct_jwt(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    url = reverse("tag_list_url")
    response = client.post(url, {"title": "test_tag_name"}, format="json")
    assert response.status_code == 201
    assert "test_tag_name" in response.data["title"]
