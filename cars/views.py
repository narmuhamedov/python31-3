from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

from django.views import generic


#Чтение из CRUD
class CarView(generic.ListView):
    template_name = 'cars/cars.html'
    queryset = models.Cars.objects.all()

    def get_queryset(self):
        return models.Cars.objects.all()



# def car_view(request):
#     cars = models.Cars.objects.all()
#     return render(request, 'cars/cars.html',
#                   {'cars': cars})


#Детальная информация
class CarDetailView(generic.DetailView):
    template_name = 'cars/car_detail.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get("id")
        return get_object_or_404(models.Cars, id=car_id)


# def car_detail_view(request, id):
#     car_id = get_object_or_404(models.Cars, id=id)
#     return render(request, 'cars/car_detail.html',
#                   {'car_id': car_id})


#Добавление объекта через формы CRUD
class CreateCarView(generic.CreateView):
    template_name = 'cars/crud/add_car.html'
    form_class = forms.CarsForm
    queryset = models.Cars.objects.all()
    success_url = '/cars/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCarView, self).form_valid(form=form)




# def create_car_view(request):
#     method = request.method
#     if method == "POST":
#         form = forms.CarsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Машина успешно добавлена в БД")
#     else:
#         form = forms.CarsForm()
#
#     return render(request, 'cars/crud/add_car.html',
#                   {"form": form})

#Удаление из БД CRUD
class CarDeleteView(generic.DeleteView):
    template_name = 'cars/crud/confirm_delete.html'
    success_url = '/cars/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Cars, id=car_id)


# def delete_car_view(request, id):
#     car_id = get_object_or_404(models.Cars, id=id)
#     car_id.delete()
#     return HttpResponse('Машина успешно удалена из БД')

#Изменение объектов в CRUD
class UpdateCarView(generic.UpdateView):
    template_name = 'cars/crud/update_car.html'
    form_class = forms.CarsForm
    success_url = '/cars/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Cars, id=car_id)

    def form_valid(self, form):
        return super(UpdateCarView, self).form_valid(form=form)

# def update_car_view(request,id):
#     car_id = get_object_or_404(models.Cars, id=id)
#     if request.method == "POST":
#         form = forms.CarsForm(instance=car_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно обновлено')
#     else:
#         form = forms.CarsForm(instance=car_id)
#
#     context = {
#         'form': form,
#         'car_id': car_id
#     }
#     return render(request, 'cars/crud/update_car.html', context)


class Search(generic.ListView):
    template_name = "cars/cars.html"
    context_object_name = "car"
    paginate_by = 5

    def get_queryset(self):
        return models.Cars.objects.filter(
            title__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context