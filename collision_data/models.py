
# Create your models here.
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=40)
    city_url = models.CharField(max_length=300)
    city_link_for_soda = models.CharField(max_length=60)
    shortener_name_soda_link = models.CharField(max_length=30, default='')


class CollisionDetails(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    borough = models.CharField(max_length=20, null=True, blank=True)
    crashDate = models.DateTimeField()
    crashTime = models.TimeField()
    zipCode = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=30, null=True, blank=True, )
    longitude = models.CharField(max_length=30, null=True, blank=True)
    crossStreetName = models.CharField(max_length=70, blank=True, null=True)
    onStreetName = models.CharField(max_length=70, default='', null=True, blank=True)
    offStreetName = models.CharField(max_length=70, default='', null=True, blank=True)
    numberOfPersonsInjured = models.IntegerField(default=0)
    numberOfPersonsKilled = models.IntegerField(default=0)
    numberOfPedestriansInjured = models.IntegerField(default=0)
    numberOfPedestriansKilled = models.IntegerField(default=0)
    numberOfCyclistInjured = models.IntegerField(default=0)
    numberOfCyclistKilled = models.IntegerField(default=0)
    numberOfMotoristInjured = models.IntegerField(default=0)
    numberOfMotoristKilled = models.IntegerField(default=0)
    contributingFactorVehicle1 = models.CharField(default='Unspecified', max_length=70, null=True, blank=True)
    contributingFactorVehicle2 = models.CharField(default='Unspecified', max_length=70, null=True, blank=True)
    collisionId = models.IntegerField()
    vehicleTypeCode1 = models.CharField(default='Unspecified', max_length=50, null=True, blank=True)
    vehicleTypeCode2 = models.CharField(default='Unspecified', max_length=50, null=True, blank=True)

    def json_to_class(self, json_data, city):
        collision_detail = json_data  # json.loads(json_data)
        self.city = city
        self.crashDate = collision_detail.get('crash_date')
        self.crashTime = collision_detail.get('crash_time')
        self.borough = collision_detail.get('borough')
        self.zipCode = collision_detail.get('zip_code')
        self.latitude = collision_detail.get('latitude')
        self.longitude = collision_detail.get('longitude')
        self.crossStreetName = collision_detail.get('cross_street_name')
        self.onStreetName = collision_detail.get('on_street_name')
        self.offStreetName = collision_detail.get('off_street_name')
        self.numberOfPersonsInjured = collision_detail.get('number_of_persons_injured')
        self.numberOfPersonsKilled = collision_detail.get('number_of_persons_killed')
        self.numberOfMotoristInjured = collision_detail.get('number_of_motorist_injured')
        self.numberOfMotoristKilled = collision_detail.get('number_of_motorist_killed')
        self.numberOfCyclistKilled = collision_detail.get('number_of_cyclist_killed')
        self.numberOfCyclistInjured = collision_detail.get('number_of_cyclist_injured')
        self.numberOfPedestriansInjured = collision_detail.get('number_of_pedestrians_injured')
        self.numberOfPedestriansKilled = collision_detail.get('number_of_pedestrians_killed')
        self.collisionId = collision_detail.get('collision_id')
        self.contributingFactorVehicle1 = collision_detail.get('contributing_factor_vehicle_1')
        self.contributingFactorVehicle2 = collision_detail.get('contributing_factor_vehicle_2')
        self.vehicleTypeCode1 = collision_detail.get('vehicle_type_code1')
        self.vehicleTypeCode2 = collision_detail.get('vehicle_type_code2')
