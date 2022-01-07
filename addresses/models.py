from django.db import models

# Create your models here.

class Addresses(models.Model):
    street = models.CharField(max_length=50)
    streetNumber = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50,  null=True)

    def __str__(self):
        return str(self.city) + " " + \
               str(self.postalCode) + "\n" + \
               str(self.street) + " " + str(self.streetNumber) + \
               "\nwojewództwo: " + str(self.district)



