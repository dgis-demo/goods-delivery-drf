import django_filters as filters

from apps.measurement.models import Currency


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CurrencyFilter(filters.FilterSet):
    currency_in = CharInFilter(field_name='currency', lookup_expr='in')
    code_in = CharInFilter(field_name='code', lookup_expr='in')
    numeric_in = CharInFilter(field_name='numeric', lookup_expr='in')
    digit_in = CharInFilter(field_name='digit', lookup_expr='in')
    country_alpha3_in = CharInFilter(
        field_name='country__alpha3', lookup_expr='in')

    order_by_field = 'ordering'

    ordering = filters.OrderingFilter(
        fields=(
            ('id', 'identifier'),
            ('code', 'code'),
        )
    )

    class Meta:
        model = Currency
        fields = (
            'currency_in', 'code_in', 'numeric_in',
            'digit_in', 'country_alpha3_in'
        )
