from django.db import models
from user.models import User

class NoteBook(models.Model):
    """
    Notebook with users notes
    """
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class Note(models.Model):
    """
    Note with users text
    """
    text = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    notebook = models.ForeignKey(NoteBook, on_delete=models.CASCADE, related_name="notebook")

    def __str__(self):
        return self.text
        