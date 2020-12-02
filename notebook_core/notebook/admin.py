from django.contrib import admin
from notebook.models import (
    NoteBook, Note,
)


models = [NoteBook, Note,]

admin.site.register(models)
