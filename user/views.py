from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions


from user.models import User
from user.serializers import SignUpSerializer


# Create your views here.
class CreateApeView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=SignUpSerializer
    permission_classes = (permissions.AllowAny,)