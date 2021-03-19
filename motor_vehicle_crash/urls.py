"""motor_vehicle_crash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from motor_vehicle_crash.views import get_city_data
from collision_data import views as collision_views
from bike_parking_info import views as bike_views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('getAllData/', collision_views.get_city_data, name='get_city_data'),
    path('getBorough/<str:borough>', collision_views.get_borough_detail),
    path('getBoroughFromDb/<str:borough>/<int:city_id>', collision_views.get_borough_detail_from_db),
    path('getCollisionDetailsFromDb/', collision_views.get_collision_details_from_db),
    path('getBikeParkingInfo/', bike_views.get_trip_data),
    path('getBikeParkingDetailsFromDb/', bike_views.get_bike_parking_details)

}
