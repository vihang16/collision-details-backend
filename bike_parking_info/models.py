from django.db import models


class BikeParkingInfo(models.Model):
    start_station_id = models.IntegerField()
    start_station_name = models.CharField(max_length=70)
    start_station_latitude = models.CharField(max_length=30)
    start_station_longitude = models.CharField(max_length=30)
    end_station_id = models.IntegerField()
    end_station_name = models.CharField(max_length=70)
    end_station_latitude = models.CharField(max_length=30)
    end_station_longitude = models.CharField(max_length=30)

    class Meta:
        db_table = "bike_parking_info"
