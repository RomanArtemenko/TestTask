from django.shortcuts import render, redirect
from productsapp.models import Product

from productsapp.forms import ProductForm 

# Create your views here.
"""
def home(request):
    # products = Product.objects.all()
    # return render(request, 'productsapp/product.html', {'products': products})
    return redirect(product)
"""
def list_product(request):
    products = Product.objects.all()
    return render(request, 'productsapp/product.html', {'products': products})

def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productsapp:product')
    return render(request, 'productsapp/add_product.html', {'form':form})

def edit_product(request, product_id):
    form = ProductForm(instance = Product.objects.get(id = product_id))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance = Product.objects.get(id = product_id))
        if form.is_valid():
            form.save()
            return redirect('productsapp:product')
    return render(request, 'productsapp/edit_product.html', {'form':form})
