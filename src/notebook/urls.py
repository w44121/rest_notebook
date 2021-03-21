from django.urls import path
from .views import (
    NoteBookListView,
    NoteBookDetailView,
    NoteListView,
    NoteDetailView,
    TagListView,
)


urlpatterns = [
    path("notebooks/", NoteBookListView.as_view(), name="notebook_list_url"),
    path("notebook/<int:pk>/", NoteBookDetailView.as_view(), name="notebook_detail_url"),
    path("notebook/<int:pk>/notes/", NoteListView.as_view(), name="note_list_url"),
    path("note/<int:pk>", NoteDetailView.as_view(), name="note_detail_url"),
    path("tag/", TagListView.as_view(), name="tag_list_url"),
]
