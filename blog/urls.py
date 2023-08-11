from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world_text, name='hello'),
    path('blog_programm_lang/', views.blog_view, name='blog'),
]