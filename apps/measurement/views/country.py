from rest_framework import mixins, viewsets

from apps.measurement.filters import CountryFilter
from apps.measurement.models import Country
from apps.measurement.serializers import CountryWithCitiesSerializer


class CountryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'list': CountryWithCitiesSerializer,
    }
    authentication_classes = ()
    filter_class = CountryFilter
    max_limit = 100

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    def get_queryset(self):
        return Country.objects.all()

    def filter_queryset(self, queryset):
        filter_class = self.filter_class(
            self.request.GET, queryset, request=self.request
        )
        queryset = filter_class.qs
        return queryset
