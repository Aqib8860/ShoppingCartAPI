from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets, status, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


# Create your views here.


class UserSerializerAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]
    http_method_names = ['post', 'head','options']

    def get_permissions(self):
        if self.action == 'post':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
