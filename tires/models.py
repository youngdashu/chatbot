from django.db import models

# Create your models here.
from tireManufacturers.models import TireManufacturers


class Tire(models.Model):

    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(TireManufacturers, on_delete=models.CASCADE)