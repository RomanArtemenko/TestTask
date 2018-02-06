from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'
        

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    name = models.CharField(max_length=30, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField('Фото', upload_to='productsapp/photos', default='', blank=True)

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты' 
    
    



