from django.db import models

# Create your models here.
from seasons.models import Seasons
from tireManufacturers.models import TireManufacturers


class Tire(models.Model):

    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(TireManufacturers, on_delete=models.CASCADE)
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20, null=True)

    def __str__(self):

        tireType = "osobowy" if str(self.type) == "car"  else "ciężarowy"

        return "Model: " + str(self.name) + " Rozmiar: " + str(self.size) +" cali Producent: " + \
               str(self.manufacturer.name) + " Sezon: " + str(self.season) + " Typ: " + tireType +\
               " Cena za oponę: " + str(self.price)