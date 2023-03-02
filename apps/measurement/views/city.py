from django.db.models.query import QuerySet
from rest_framework import mixins, viewsets

from apps.measurement.models import City
from apps.measurement.serializers import CityWithStoresSerializer


class CityViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'retrieve': CityWithStoresSerializer,
        # 'metadata': CitySerializer,
    }
    authentication_classes = ()
    max_limit = 100

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    def get_queryset(self) -> QuerySet:
        return City.objects.all()
