from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status, views
from rest_framework import permissions, authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    NoteSerializer, NoteBookSerializer
)
from .models import (
    Note, NoteBook,
)


class NoteBookListView(views.APIView):
    def get(self, request):
        notebooks = NoteBook.objects.all()
        serializer = NoteBookSerializer(notebooks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteBookDetailView(views.APIView):
    def _try_get_notebook(self, pk):
        try:
            return NoteBook.objects.get(pk=pk)
        except NoteBook.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        notebook = self._try_get_notebook(pk)
        serializer = NoteBookSerializer(notebook)
        # data = {
        #     "number of notes": Note.objects.filter(notebook__id=pk).count()
        # }
        return Response(serializer.data)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


class NoteListView(views.APIView):
    def get(self, request, pk):
        notes = Note.objects.filter(notebook__id=pk)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetailView(views.APIView):
    def _try_get_note(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        note = self._try_get_note(pk)
        serializer = NoteSerializer(note)
        return Response(serializers.data)

    def put(self, request):
        pass

    def delete(self, request):
        pass
