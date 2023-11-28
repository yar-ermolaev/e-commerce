from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name='URL')
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель')
    in_stock = models.PositiveIntegerField(default=0,
                                           verbose_name='Остаток на складе')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                verbose_name='Цена')
    properties = models.JSONField(blank=True, verbose_name='Характеристики')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image_paths = models.JSONField(blank=True, verbose_name='Список изображений')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 related_name='products')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image_path = models.CharField(max_length=255, unique=True,
                                  verbose_name='Расположение')
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='images', verbose_name='Продукт')


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True,
                            verbose_name='URL')

    def __str__(self):
        return self.name
