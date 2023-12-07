from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', views.ShowCart.as_view(), name='cart_details'),
]