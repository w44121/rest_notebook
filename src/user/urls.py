from django.urls import path
from user.views import UserRegistration


urlpatterns = [
    path("registration/", UserRegistration.as_view(), name="registration_url"),
]
