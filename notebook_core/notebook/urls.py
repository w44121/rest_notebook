from django.urls import path, include
from rest_framework import routers
from .views import (
    NoteBookListView,
    NoteBookDetailView,
    NoteListView,
    NoteView,
)

router = routers.DefaultRouter()
router.register("note", NoteView)

urlpatterns = [
    path("notebooks/", NoteBookListView.as_view()),
    path("notebook/<int:pk>/", NoteBookDetailView.as_view()),
    path("notebook/<int:pk>/notes/", NoteListView.as_view()),
]


urlpatterns += router.urls
