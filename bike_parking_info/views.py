from django.http import JsonResponse, HttpResponse
from .utils import get_data_from_url

import logging
from .models import BikeParkingInfo
from django.core import serializers


def get_trip_data(request):
    df = get_data_from_url()
    logging.info('creating model instances')
    model_instances = [BikeParkingInfo(
        start_station_id=raw['start station id'],
        start_station_name=raw['start station name'],
        start_station_latitude=raw['start station latitude'],
        start_station_longitude=raw['start station longitude'],
        end_station_id=raw['end station id'],
        end_station_name=raw['end station name'],
        end_station_latitude=raw['end station latitude'],
        end_station_longitude=raw['end station longitude'],
    ) for _, raw in df.iterrows()]
    logging.info('model instances created succesfully, storing into db')
    BikeParkingInfo.objects.bulk_create(model_instances)
    df.reset_index(drop=True, inplace=True)
    return JsonResponse(df.to_json(), safe=False)


def get_bike_parking_details(request):
    all_bike_details = BikeParkingInfo.objects.all()
    serialize_data = serializers.serialize('json', all_bike_details)
    response = HttpResponse(serialize_data, content_type="text/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    return response
