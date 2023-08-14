from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_view, name='cars'),
    path('cars_detail/<int:id>/', views.car_detail_view, name='cars_detail'),
]