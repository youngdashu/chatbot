from django.db import models

# Create your models here.
from addresses.models import Addresses


class CarWorkshops(models.Model):

    name = models.CharField(max_length=50)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=20)
    emailAddress = models.EmailField(max_length=50)
