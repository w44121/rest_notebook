from django.urls import path, include
from rest_framework import routers
from .views import (
    NoteBookListView,
    NoteBookDetailView,
    NoteListView,
    NoteDetailView,
)


urlpatterns = [
    path("notebooks/", NoteBookListView.as_view(), name="notebook_list_url"),
    path("notebook/<int:pk>/", NoteBookDetailView.as_view(), name="notebook_detail_url"),
    path("notebook/<int:pk>/notes/", NoteListView.as_view()),
    path("note/<int:pk>", NoteDetailView.as_view()),
]
