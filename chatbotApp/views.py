from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from seasons.models import Seasons
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


def addSeasons(requests, *args, **kwargs):
    summer = Seasons(name="summer")
    summer.save()
    winter = Seasons(name="winter")
    winter.save()
    all_seasons = Seasons(name="all_seasons")
    all_seasons.save()
    return HttpResponse("successful")


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
    seasons = Seasons.objects.all()
    names = ["Passjo", "Frigo", "Navigator"]
    sizes = [13, 14, 15]
    prices = [183.5, 209.0, 228.5]
    m = TireManufacturers.objects.get(name__startswith="Dęb")
    for name, size, price, season in zip(names, sizes, prices, seasons):
        tire = Tire(name=name, size=size, price=price, manufacturer=m, season=season, type="car")
        tire.save()

    sizes = [22]
    prices = [3423.9]
    m = TireManufacturers.objects.get(name__startswith="Good")
    for size, price, season in zip(sizes, prices, seasons):
        tire = Tire(name="Kmax s gen 2", size=size, price=price, manufacturer=m, season=season, type="truck")
        tire.save()

    return HttpResponse("successful")


@csrf_exempt
@require_POST
def dialogflowRequest(request):
    def getListOfAvailableTires(req):

        outputContexts = req['queryResult']['outputContexts']
        season = None
        size = None
        carType = None
        for outputContext in outputContexts:
            parameters = outputContext['parameters']
            if season is None and parameters.get('tire-season') is not None:
                season = parameters.get('tire-season')
            if size is None and parameters.get('number') is not None:
                size = parameters.get('number')
            if carType is None and parameters.get('car-type') is not None:
                carType = parameters.get('car-type')
        seasonObj = Seasons.objects.filter(name__startswith=season)

        tires = Tire.objects.filter(season__tire=seasonObj, size__in=[size], type=carType)

        res = ""
        for tire in tires:
            res += (str(tire) + "\n")
        return res

    body = request.body.decode().replace("\n", "")
    # print(body)
    req = json.loads(body)

    responseText = "Default django response"

    parameters = req['queryResult'].get('parameters')
    if parameters:

        if parameters.get('tire-season') is not None:
            responseText = getListOfAvailableTires(req)

        elif parameters.get('number') is not None:
            # check tire size
            tireSize = Tire.objects.filter(size__in=[req['queryResult']['parameters']['number']])

            if len(tireSize) == 0:
                responseText = "Brak opon o podanym rozmiarze"
            else:
                responseText = "W porządku, na jaką porę roku potrzebujesz opon? Letnie, zimowe, całoroczne"

        else:
            pass

    res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

    return JsonResponse(res)
