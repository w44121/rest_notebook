from django.http import Http404
from rest_framework import viewsets, status, views
from rest_framework import permissions
from rest_framework.response import Response
from notebook.serializers import (
    NoteSerializer, NoteBookSerializer
)
from notebook.models import (
    Note, NoteBook,
)


class NoteBookListView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notebooks = NoteBook.objects.filter(author__id=request.user.id)
        serializer = NoteBookSerializer(notebooks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteBookSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteBookDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def _try_get_notebook(self, pk):
        try:
            return NoteBook.objects.get(pk=pk)
        except NoteBook.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        notebook = self._try_get_notebook(pk)
        serializer = NoteBookSerializer(notebook)
        return Response(serializer.data)
    
    def put(self, request, pk):
        notebook = self._try_get_notebook(pk)
        serializer = NoteBookSerializer(notebook, data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notebook = self._try_get_notebook(pk)
        notebook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteListView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        notes = Note.objects.filter(notebook__id=pk)
        if not NoteBook.objects.filter(pk=pk):
            raise Http404
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def _try_get_note(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        note = self._try_get_note(pk)
        serializer = NoteSerializer(note)
        return Response(serializers.data)

    def put(self, request, pk):
        note = self._try_get_note(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self._try_get_note(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
