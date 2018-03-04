from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
