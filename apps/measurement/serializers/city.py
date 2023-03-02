from rest_framework import serializers

from apps.measurement.models import City


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields: tuple = (
            'id',
            'name',
        )


class CityWithStoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields: tuple = (
            'name',
        )
