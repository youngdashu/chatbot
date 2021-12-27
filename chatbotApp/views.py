from django.shortcuts import render
from django.http import HttpResponse

from addresses.models import Addresses


def test(requests, *args, **kwargs):

    sampleAddress = Addresses(street="Długa", streetNumber=12, postalCode="69-420", city="Kraków")
    sampleAddress.save()
    return HttpResponse("record saved")

def testNumbers(requests, *args, **kwargs):
    sampleAddress = Addresses(street="Długa", streetNumber=kwargs["number"], postalCode="69-420", city="Kraków")
    sampleAddress.save()
    return HttpResponse("record saved")

