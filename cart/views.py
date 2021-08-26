from django.shortcuts import render
from rest_framework.decorators import api_view, APIView, action
from .serializers import *
from .models import *
from core.models import User
from rest_framework import viewsets, status, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


# Create your views here.


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['post', 'head','options']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ViewCartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['get', 'head','options']

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user).order_by('date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EditCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = UpdateCartSerializer

    def get(self, request, *args, **kwargs):
        try:
            queryset = Cart.objects.get(id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Cart Id Does not exist"}, status=400)
        if Cart.objects.filter(id=self.kwargs["pk"], user=request.user).exists():
            serializer = self.get_serializer(queryset)
            return Response(serializer.data, status=200)
        else:

            return Response({"DOES_NOT_EXIST": "You are not the user of this cart id"}, status=400)

    def put(self, request, *args, **kwargs):
        try:
            queryset = Cart.objects.get(id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Cart Id Does not exist"}, status=400)
        if Cart.objects.filter(id=self.kwargs["pk"], user=request.user).exists():
            return self.update(request, *args, **kwargs)
        else:
            return Response({"DOES_NOT_EXIST":"You are not the user of this cart "}, status=400)

    def delete(self, request, *args, **kwargs):
        if Cart.objects.filter(id=self.kwargs["pk"], user=request.user).exists():
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({"DOES_NOT_EXIST": "You are not the user of this cart id"}, status=400)
