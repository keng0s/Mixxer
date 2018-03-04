from django.db import models
from drinks.models import Drink
from components.models import Component


class Recipe(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT, related_name='recipes')
    component = models.ForeignKey(Component, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
