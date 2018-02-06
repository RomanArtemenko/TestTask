from django.shortcuts import render
from productsapp.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'productsapp/home.html', {'products': products})