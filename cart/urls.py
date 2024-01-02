from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/', views.AddToCartView.as_view(), name='add'),
    path('cart/', views.ShowCart.as_view(), name='cart_details'),
    path('delete_cart_item/<int:item_pk>/', views.DeleteFromCartView.as_view(),
         name='delete_cart_item'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]
