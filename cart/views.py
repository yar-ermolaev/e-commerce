from django.db.models import F, fields, ExpressionWrapper, Sum
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from products.models import Product
from .models import CartItem, Cart


class AddToCartView(View):
    template_name = 'products/show_product.html'

    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('category_detail', product.category.slug)


class ShowCart(ListView):
    template_name = 'cart/cart_details.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart).annotate(
            total=F('quantity') * F('product__price')
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = self.get_queryset().aggregate(total_price=Sum('total'))['total_price']
        context['total_price'] = total_price
        return context
