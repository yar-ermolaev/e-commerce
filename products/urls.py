from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.ProductView.as_view()),
]