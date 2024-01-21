import django_filters

from .models import Product


class AllValuesByCategory(django_filters.MultipleChoiceFilter):
    @property
    def field(self):
        qs = self.parent.queryset
        qs = qs.order_by(self.field_name).values_list(self.field_name, flat=True).distinct()
        self.extra["choices"] = [(o, o) for o in qs]
        return super().field


class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(
        field_name='price', lookup_expr='range', label='Цена',
    )

    manufacturer = AllValuesByCategory(
        field_name='manufacturer', label='Бренд'
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
