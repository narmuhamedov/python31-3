from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarView.as_view(), name='cars'),
    path('cars_detail/<int:id>/', views.CarDetailView.as_view(), name='cars_detail'),
    path('cars_detail/<int:id>/delete/', views.CarDeleteView.as_view(), name='cars_delete'),
    path('cars_detail/<int:id>/update/', views.UpdateCarView.as_view(), name='cars_update'),
    path('add-cars/', views.CreateCarView.as_view(), name='add_car'),
    path('search/', views.Search.as_view(), name='search')
]
