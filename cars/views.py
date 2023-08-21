from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

#Чтение из CRUD
def car_view(request):
    cars = models.Cars.objects.all()
    return render(request, 'cars/cars.html',
                  {'cars': cars})

def car_detail_view(request, id):
    car_id = get_object_or_404(models.Cars, id=id)
    return render(request, 'cars/car_detail.html',
                  {'car_id': car_id})


#Добавление объекта через формы CRUD
def create_car_view(request):
    method = request.method
    if method == "POST":
        form = forms.CarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Машина успешно добавлена в БД")
    else:
        form = forms.CarsForm()

    return render(request, 'cars/crud/add_car.html',
                  {"form": form})

#Удаление из БД CRUD
def delete_car_view(request, id):
    car_id = get_object_or_404(models.Cars, id=id)
    car_id.delete()
    return HttpResponse('Машина успешно удалена из БД')

#Изменение объектов в CRUD
def update_car_view(request,id):
    car_id = get_object_or_404(models.Cars, id=id)
    if request.method == "POST":
        form = forms.CarsForm(instance=car_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно обновлено')
    else:
        form = forms.CarsForm(instance=car_id)

    context = {
        'form': form,
        'car_id': car_id
    }
    return render(request, 'cars/crud/update_car.html', context)