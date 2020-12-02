from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_user_registration_valid_data(client):
    url = reverse("registration_url")
    response = client.post(url, {
        "username": "test_user_for_reg", 
        "password": "qwerty123"})
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_registration_when_user_is_already_in_db(client, user):
    url = reverse("registration_url")
    response = client.post(url, {
        "username": user.username, 
        "password": user.password})
    assert response.data == {"username": ["A user with that username already exists."]}
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_registration_with_blank_fields(client):
    url = reverse("registration_url")
    response = client.post(url, {
        "username": "", 
        "password": ""})
    assert response.data["username"] == ["This field may not be blank."]
    assert response.data["password"] == ["This field may not be blank."]
    assert response.status_code == 400
