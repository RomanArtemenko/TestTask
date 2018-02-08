from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from productsapp.models import Product, Category, ProductType

from productsapp.forms import ProductForm, CategoryForm, ProductTypeForm 

from django.views.generic import View
from django.http import JsonResponse
import json

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
    return render(request, 'productsapp/add_product.html', {'form': form})

def edit_product(request, product_id):
    #form = ProductForm(instance = Product.objects.get(id = product_id))
    form = ProductForm(instance = get_object_or_404(Product, pk=product_id))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance = Product.objects.get(id = product_id))
        if form.is_valid():
            form.save()
            return redirect('productsapp:product')
    return render(request, 'productsapp/edit_product.html', {'form': form})

def category(request):
    categories = Category.objects.all()
    return render(request, 'productsapp/category.html', {'categories': categories})

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productsapp:category')
    return render(request, 'productsapp/add_category.html', {'form': form})

def product_type(request):
    types = ProductType.objects.all()
    return render(request, 'productsapp/product_type.html', {'types': types})

def add_product_type(request):
    form = ProductTypeForm()
    if request.method == 'POST':
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productsapp:product-type')
    return render(request, 'productsapp/add_product_type.html', {'form': form})

class ProductView(View):
    templateName = 'productsapp/product.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.templateName, {'products': products})

    def post(self, request):
        if request.is_ajax():
            data = json.loads(request.body.decode("utf-8"))
            query = data.get('query')
        
            products = Product.objects.filter(name__icontains=query)
            
            return render(request, 'productsapp/ajax.html', {'products': products})
        else:
            JsonResponse({'msg': 'This is no ajax request'}, status=400)
