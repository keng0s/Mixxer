from rest_framework import serializers
from .models import Recipe
from components.serializers import ComponentSerializer


class RecipeSerializer(serializers.ModelSerializer):

    component = ComponentSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'component', 'amount')
