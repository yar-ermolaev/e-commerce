from pathlib import Path

from django.views.generic import DetailView, ListView
from .models import Product


class ProductView(DetailView):
    model = Product
    template_name = 'products/show_product.html'
    context_object_name = 'product'


class CategoryProducts(ListView):
    model = Product
    template_name = 'products/category_details.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        return queryset.filter(category__slug=self.kwargs['slug'])


