from django.urls import path

from . import views

app_name = 'productsapp'
urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.list_product, name='product'),
    path('product/add', views.add_product, name='add-product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit-product'),
    path('category/', views.category, name='category'),
    path('category/add', views.add_category, name='add-category'),
    path('product-type/', views.product_type, name='product-type'),
    path('product-type/add', views.add_product_type, name='add-product-type'),

]