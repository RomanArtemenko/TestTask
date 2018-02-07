from django import forms
from productsapp.models import Product, Category, ProductType

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'