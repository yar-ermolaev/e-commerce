from pathlib import Path

from django.views.generic import DetailView, ListView
from .models import Product, Category


class ProductView(DetailView):
    model = Product
    template_name = 'products/show_product.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CategoryList(ListView):
    model = Category
    template_name = 'products/show_categories.html'
    context_object_name = 'categories'


class CategoryDetails(DetailView):
    model = Category
    template_name = 'products/category_details.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()[:10]
        return context


