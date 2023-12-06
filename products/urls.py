from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(
        template_name='products/show_categories.html'
        ), name='index'),
    path('categories/<slug:slug>/',
         views.CategoryProducts.as_view(), name='category_detail'),
    path('categories/<slug:cat_slug>/<slug:slug>/',
         views.ProductView.as_view(), name='product_detail'),
]