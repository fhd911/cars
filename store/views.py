from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'store-templates/home.html')


def products_list(request):
    products = Product.objects.all()
    return render(request, 'store-templates/products.html', {'products': products})
