from rest_framework import serializers
from .models import Meal
from applications.menu.serializers import MenuSerializer
class MealSerializer(serializers.ModelSerializer):
    
    #menu = MenuSerializer(read_only=True)

    class Meta:
        model = Meal
        fields = (
            'description',
            'menu'
        )    

