from django.contrib import admin
from productsapp.models import Category, ProductType, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Product)