from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view()),
    path('<slug:slug>/', views.ProductView.as_view()),
]