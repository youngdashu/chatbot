from django.db import models

# Create your models here.

class Addresses(models.Model):
    street = models.CharField(max_length=50)
    streetNumber = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length="50")

