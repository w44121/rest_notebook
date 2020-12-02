from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import views, status
from rest_framework.response import Response
from user.serializers import UserSerializer


class UserRegistration(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
