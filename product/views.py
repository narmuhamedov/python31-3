from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models

class ProductView(ListView):
    template_name = 'product/product.html'
    #queryset = models.Product.objects.all()
    #queryset = models.Product.objects.filter().order_by('-id')
    queryset = models.Product.objects.filter(tag__name_tag='электроника')

    def get_queryset(self):
        #return models.Product.objects.all()
        #return models.Product.objects.filter().order_by('-id')
        return models.Product.objects.filter(tag__name_tag='электроника')





class DetailProductView(DetailView):
    template_name = 'product/product_detail.html'

    def get_object(self, *args, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=product_id)

