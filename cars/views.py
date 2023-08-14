from django.shortcuts import render, get_object_or_404
from . import models

def car_view(request):
    cars = models.Cars.objects.all()
    return render(request, 'cars/cars.html',
                  {'cars': cars})

def car_detail_view(request, id):
    car_id = get_object_or_404(models.Cars, id=id)
    return render(request, 'cars/car_detail.html',
                  {'car_id': car_id})

