from django.contrib import admin
from notebook.models import (
    NoteBook, Note, Tag,
)


models = [NoteBook, Note, Tag, ]

admin.site.register(models)
