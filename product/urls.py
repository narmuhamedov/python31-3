from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('product_detail/<int:id>/', views.DetailProductView.as_view(), name='detail'),
]