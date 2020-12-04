from rest_framework import serializers
from notebook.models import NoteBook
from user.models import User
from .models import (
    NoteBook, Note
)


class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = "__all__"

    def validate(self, data):
        if not self.context["user"].premium:
            if NoteBook.objects.filter(author__id=self.context["user"].id).count() < 5:
                return data
            raise serializers.ValidationError({"error": "only premium users can have more then 5 notebooks"})
        return data
    
    def create(self, data):
        return NoteBook.objects.create(**data, author=self.context["user"])


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
