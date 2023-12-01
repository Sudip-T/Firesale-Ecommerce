from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import * 


class StoreView(ListView):
    model = Product
    template_name = 'index.html'


class ProductView(DetailView):
    model = Product
    template_name = 'product.html'


def add_to_cart(request):
    pass
