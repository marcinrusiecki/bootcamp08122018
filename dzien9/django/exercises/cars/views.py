from django.shortcuts import render
from cars.models import Car
# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    return render(
        request = request,
        template_name = "cars_list.html",
        context = {"cars": cars}
    )

def car_details(request,id):
    car = Car.objects.get(id=id)
    return render(
        request = request,
        template_name = "details.html",
        context = {"car": car}
    )


