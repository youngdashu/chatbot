from django.db import models


# Create your models here.


class Seasons(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):

        if self.name == "summer":
            return "lato"
        elif self.name == "winter":
            return "zima"
        elif self.name == "all_seasons":
            return "całoroczne"
        else:
            raise RuntimeError()
