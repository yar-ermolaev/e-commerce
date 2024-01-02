from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                related_name='cart')
    products = models.ManyToManyField('products.Product', through='CartItem')
    session_key = models.CharField(max_length=32, null=True, blank=True)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
