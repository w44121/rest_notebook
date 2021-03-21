from django.conf import settings
from rest_framework import serializers
from .models import (
    NoteBook, Note, Tag,
)


class NoteBookSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = NoteBook
        fields = "__all__"

    def validate(self, data):
        data["author"] = self.context["user"]
        if not self.context["user"].premium:
            if NoteBook.objects.filter(author__id=self.context["user"].id).count() < settings.MAX_NOTEBOOKS_FOR_NO_PREMIUM_USERS:
                return data
            raise serializers.ValidationError({"error": "only premium users can have more then 5 notebooks"})
        return data


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    def validate(self, data):
        data["author"] = self.context["user"]
        return data
