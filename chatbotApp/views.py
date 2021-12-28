from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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


def addTireManufacturers(requests, *args, **kwargs):
    manufacturerNames = ["Dębica", "Goodyear", "Dunlop", "Fulda"]
    for manufacturerName in manufacturerNames:
        manufacturer = TireManufacturers(manufacturerName)
        manufacturer.save()

    q = TireManufacturers.objects.all()
    print(q)


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
