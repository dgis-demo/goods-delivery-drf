from rest_framework import mixins, viewsets

from apps.measurement.filters import CurrencyFilter
from apps.measurement.models import Currency
from apps.measurement.serializers import CurrencySerializer


class CurrencyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'list': CurrencySerializer,
        'retrieve': CurrencySerializer,
        'metadata': CurrencySerializer,
    }
    authentication_classes = ()
    filter_class = CurrencyFilter
    max_limit = 100

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    def get_queryset(self):
        return Currency.objects.all()

    def filter_queryset(self, queryset):
        filter_class = self.filter_class(
            self.request.GET, queryset, request=self.request
        )
        queryset = filter_class.qs
        return queryset
