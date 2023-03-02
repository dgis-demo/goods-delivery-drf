import django_filters as filters

from apps.measurement.models import Country


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CountryFilter(filters.FilterSet):
    full_name_in = CharInFilter(field_name='full_name', lookup_expr='in')
    short_name_in = CharInFilter(field_name='short_name', lookup_expr='in')
    alpha2_in = CharInFilter(field_name='alpha2', lookup_expr='in')
    alpha3_in = CharInFilter(field_name='alpha3', lookup_expr='in')
    code_in = CharInFilter(field_name='code', lookup_expr='in')

    order_by_field = 'ordering'

    ordering = filters.OrderingFilter(
        fields=(
            ('id', 'identifier'),
            ('alpha3', 'alpha3'),
        )
    )

    class Meta:
        model = Country
        fields = (
            'full_name_in', 'short_name_in', 'alpha2_in',
            'alpha3_in', 'code_in'
        )
