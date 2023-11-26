from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                verbose_name='Цена')
    in_stock = models.PositiveIntegerField(default=0,
                                           verbose_name='Остаток на складе')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name
