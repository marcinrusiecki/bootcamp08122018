from django.urls import path
from cars.views import car_list
from cars.views import car_details

urlpatterns = [
    path('', car_list, name='cars_list'),
    path('<int:id>', car_details)
]