from rest_framework import serializers

from apps.measurement.models import Country

from .city import CityListSerializer


class CountryWithCitiesSerializer(serializers.ModelSerializer):
    """"""
    cities = CityListSerializer(many=True)

    class Meta:
        model = Country
        fields: tuple = (
            'id',
            'short_name',
            'cities',
        )
