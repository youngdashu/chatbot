from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from tireManufacturers.models import TireManufacturers
from tires.models import Tire

import json

from addresses.models import Addresses


def test(requests, *args, **kwargs):
    sampleAddress = Addresses(street="Długa", streetNumber=12, postalCode="69-420", city="Kraków")
    sampleAddress.save()
    return HttpResponse("record saved")


def testNumbers(requests, *args, **kwargs):
    sampleAddress = Addresses(street="Długa", streetNumber=kwargs["number"], postalCode="69-420", city="Kraków")
    sampleAddress.save()
    return HttpResponse("record saved")


@require_GET
def addTireManufacturers(requests, *args, **kwargs):
    manufacturerNames = ["Dębica", "Goodyear", "Dunlop", "Fulda"]
    for manufacturerName in manufacturerNames:
        manufacturer = TireManufacturers(name=manufacturerName)
        manufacturer.save()

    q = TireManufacturers.objects.all()
    print(q)

    return HttpResponse("successfully added")


@require_GET
def addTire(requests, *args, **kwargs):
    sizes = [13, 14, 15]
    prices = [183.5, 209.0, 228.5]
    m = TireManufacturers.objects.get(name__startswith="Dęb")
    for size, price in zip(sizes, prices):
        tire = Tire(name="Frigo", size=size, price=price, manufacturer=m)
        tire.save()

    return HttpResponse("successful")


@csrf_exempt
@require_POST
def dialogflowRequest(request):
    # print(request)
    # print(request.POST)
    # print(request.body)
    # print(str(request.body))

    body = request.body.decode().replace("\n", "")
    # print(body)
    req = json.loads(body)

    responseText = "Default django response"

    if req['queryResult']['parameters']['number'] is not None:
        # check tire size
        tireSize = Tire.objects.filter(size__in=[req['queryResult']['parameters']['number']])

        if len(tireSize) == 0:
            responseText = "Brak opon o podanym rozmiarze"
        else:
            responseText = "W porządku, na jaką porę roku potrzebujesz opon?"

    else:
        pass

    res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

    return JsonResponse(res)
