# Generated by Django 2.0.2 on 2018-02-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0002_auto_20180205_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='productsapp/photos', verbose_name='Фото'),
        ),
    ]