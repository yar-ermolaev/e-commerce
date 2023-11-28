from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view()),
    path('<slug:slug>/', views.CategoryDetails.as_view(), name='category_detail'),
    path('<slug:cat_slug>/<slug:slug>/', views.ProductView.as_view(), name='product_detail'),
]