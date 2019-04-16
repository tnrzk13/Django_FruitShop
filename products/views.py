from django.shortcuts import render
from django.http import HttpResponse
from .models import Product   #use the Product class

# Create your views here.

#map /products url -> index
def index(request):
    #Product.objects.all() returns all objs in database
    #Product.objects.filter() returns all objs in database
    #Product.objects.get() gets a product
    #Product.objects.save() inserts an existing product
    products = Product.objects.all()
    return render(request, 
                "index.html", #template name
                {"products": products}) #dictionary to be passed into template


def new(request):
    return HttpResponse("New Products")

