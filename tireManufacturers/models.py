from django.db import models

# Create your models here.


class TireManufacturers(models.Model):

    name = models.CharField(max_length=50)

    def __repr__(self):
        return self.name.__repr__()
