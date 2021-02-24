from django.shortcuts import render, HttpResponse
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)

from .models import Order
from .serializers import OrderSerializer


class OrderListApiView(ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.all()

class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter()

class OrderCreateApiView(CreateAPIView):
    serializer_class = OrderSerializer

class OrderDeleteView(DestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.filter()

class OrderUpdateView(RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.filter()
