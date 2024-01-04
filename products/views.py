from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import DetailView, ListView
from .models import Product


class ProductView(DetailView):
    model = Product
    template_name = 'products/show_product.html'
    context_object_name = 'product'


class CategoryProducts(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))


class SearchProducts(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        vector = SearchVector('name', 'description')
        query = SearchQuery(query)
        return Product.objects.annotate(
            rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
