from rest_framework import serializers
from .models import Order
from applications.meals.serializers import MealSerializer

class OrderSerializer(serializers.ModelSerializer):

    meal = MealSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'details',
            'meal',
        )

