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

    def __repr__(self):
        return "Model: " + str(self.name) + " rozmiar: " + str(self.size) +" cali producent: " + \
               str(self.manufacturer.name) + " sezon: " + str(self.season) + " typ: " + str(self.type) +\
               " cena za oponę: " + str(self.price)