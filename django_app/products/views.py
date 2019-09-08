from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    # get all data from the database
    products = Product.objects.all()
    # return HttpResponse("THis are the products")
    return render(request, 'index.html', {'products': products})


def newProduct(request):
    return HttpResponse("Enter the new product here ...")
