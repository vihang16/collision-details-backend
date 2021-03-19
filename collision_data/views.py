from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from sodapy import Socrata
from .models import City, CollisionDetails
from django.core import serializers
from django.db.models import Q
import logging as log


def get_city_data(request):
    all_cities = City.objects.all()
    results = []
    assert isinstance(all_cities, object)
    for city in all_cities:
        client = Socrata(city.city_link_for_soda, None)
        json_data = client.get(city.shortener_name_soda_link)
        print(len(json_data))
        for json_str in json_data:
            if is_new_data(json_str, city):
                collision_obj = CollisionDetails()
                collision_obj.json_to_class(json_str, city)
                collision_obj.save()
        results.append(json_data)
    return JsonResponse(results, safe=False)


def get_borough_detail(request, borough):
    client = Socrata("data.cityofnewyork.us", None)
    where_clause = 'borough="' + borough.upper() + '" and (number_of_cyclist_injured > 0 or number_of_cyclist_killed>0)'
    log.info(where_clause)
    results = client.get("h9gi-nx95", where=where_clause)
    return JsonResponse(results, safe=False)


def get_borough_detail_from_db(request, borough, city_id):
    result = CollisionDetails.objects.filter(borough=borough.upper()).filter(city_id=city_id).exclude(
        latitude='').exclude(longitude='')
    serialize_data = serializers.serialize('json', result)
    return HttpResponse(serialize_data, content_type="text/json")


def get_collision_details_from_db(request):
    query = (Q(numberOfCyclistInjured__gt=0) | Q(numberOfCyclistKilled__gt=0)) & (
                ~Q(longitude='') & ~Q(latitude='') & ~Q(longitude__isnull=True) & ~Q(latitude__isnull=True))

    # result = CollisionDetails.objects.exclude(numberOfCyclistInjured__gt=1).exclude(numberOfCyclistKilled__gt=1).filter(latitude='').filter(longitude='')
    result = CollisionDetails.objects.filter(query)
    serialize_data = serializers.serialize('json', result)
    return HttpResponse(serialize_data, content_type="text/json")


def is_new_data(collison_details, city):
    result = CollisionDetails.objects.filter(city=city).filter(collisionId=int(collison_details.get('collision_id')))
    if result.exists():
        log.info("object is present in db:"+collison_details.get('collision_id'))
        return False

    return True

