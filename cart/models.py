from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                related_name='cart')
    products = models.ManyToManyField('products.Product', through='CartItem')
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        if self.user:
            return f'Корзина пользователя {self.user}'
        else:
            return f'Корзина анонимного пользователя, ключ сессии {self.session_key}'


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'Товар {self.product} - {self.cart}'
