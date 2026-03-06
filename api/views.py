from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from api.serializers import UserRegisterSerializer


class UserRegisterApiView(CreateAPIView):
    serializer_class = UserRegisterSerializer

