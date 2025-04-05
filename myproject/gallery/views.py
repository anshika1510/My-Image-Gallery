from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def home(request):
    return render(request, 'gallery/home.html')

def homepage(request):
    return render(request, 'gallery/homepage.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'gallery/index.html', {'products': products})

def slideshow_view(request):
    # We fetch all Product objects, assuming each product has an image
    images = Product.objects.all()
    return render(request, 'gallery/slideshow.html', {'images': images})


