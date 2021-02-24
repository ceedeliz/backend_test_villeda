from django.shortcuts import render, HttpResponse
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)

from .models import Meal
from .serializers import MealSerializer


class MealListApiView(ListAPIView):
    serializer_class = MealSerializer
    def get_queryset(self):
        return Meal.objects.all()

class MealDetailView(RetrieveAPIView):
    serializer_class = MealSerializer
    def get_queryset(self):
        return Meal.objects.filter()

class MealActiveView(ListAPIView):
    serializer_class = MealSerializer
    def get_queryset(self):
        fk = self.kwargs['fk']
        return Meal.objects.filter(menu_id__id=fk)

class MealCreateApiView(CreateAPIView):
    serializer_class = MealSerializer

class MealDeleteView(DestroyAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.filter()

class MealUpdateView(RetrieveUpdateAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.filter()
