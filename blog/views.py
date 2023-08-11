from django.http import HttpResponse
from django.shortcuts import render
from . import models

#Логика для отображения какого текста
def hello_world_text(request):
    return HttpResponse("Hello this is my first project Django\n"
                        "Hello World")

#логика для отображения на веб странице нашего блога
def blog_view(request):
    blog = models.BlogProgramLang.objects.all()
    return render(request, 'blog.html', {'blog': blog})