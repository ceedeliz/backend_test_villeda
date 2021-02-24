from datetime import date
from django.shortcuts import render, HttpResponse
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)

from .models import Menu
from .serializers import MenuSerializer


class MenuListApiView(ListAPIView):
    serializer_class = MenuSerializer
    def get_queryset(self):
        return Menu.objects.all()

class MenuDetailView(RetrieveAPIView):
    serializer_class = MenuSerializer
    def get_queryset(self):
        return Menu.objects.filter()

class MenuActiveView(ListAPIView):
    serializer_class = MenuSerializer
    def get_queryset(self):
        return Menu.objects.filter(day__gte=date.today()).order_by('day')

class MenuCreateApiView(CreateAPIView):
    serializer_class = MenuSerializer

class MenuDeleteView(DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter()

class MenuUpdateView(RetrieveUpdateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter()
