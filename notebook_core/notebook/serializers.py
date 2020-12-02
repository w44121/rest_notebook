from rest_framework import serializers
from .models import (
    NoteBook, Note
)


class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        depth = 1
