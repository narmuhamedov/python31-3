from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_view, name='cars'),
    path('cars_detail/<int:id>/', views.car_detail_view, name='cars_detail'),
    path('cars_detail/<int:id>/delete/', views.delete_car_view, name='cars_delete'),
    path('cars_detail/<int:id>/update/', views.update_car_view, name='cars_update'),
    path('add-cars/', views.create_car_view, name='add_car'),
]
