# backend/src/backend/users/views.py
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        r = super().create(request, *args, **kwargs)
        return Response({"detail": "회원가입 성공"}, status=status.HTTP_201_CREATED)

