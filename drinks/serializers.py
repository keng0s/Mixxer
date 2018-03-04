from rest_framework import serializers
from .models import Drink
from recipes.serializers import RecipeSerializer


class DrinkSerializer(serializers.ModelSerializer):

    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Drink
        fields = (
            'id',
            'name',
            'volume',
            'recipes'
        )
