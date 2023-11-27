from pathlib import Path

from django.views.generic import DetailView
from .models import Product


class ProductView(DetailView):
    model = Product
    template_name = 'products/show_product.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     paths = context.get('product').image_paths
    #     context['image_paths'] = [str(Path('media/', file_path)) for file_path in paths]
    #     return context
