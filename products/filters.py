import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        manufacturers = Product.objects.filter(
            category__slug=self.request.resolver_match.kwargs.get('slug')).values_list(
            'manufacturer', flat=True).distinct().order_by('manufacturer')
        self.filters['manufacturer'].extra['choices'] = [(choice, choice) for choice in manufacturers]

    price = django_filters.RangeFilter(
        field_name='price', lookup_expr='range', label='Цена',
    )
    manufacturer = django_filters.MultipleChoiceFilter(
        label='Бренд', choices=[],
    )

    ordering = django_filters.OrderingFilter(
        label='Сортировка',
        fields=(
            ('price', 'price')
        ),
        choices=(
            ('price', 'Сначала дешевле'),
            ('-price', 'Сначала дороже'),
        ),
        empty_label='По умолчанию'
    )

    class Meta:
        model = Product
        fields = ['price', 'manufacturer']
