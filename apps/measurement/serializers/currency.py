from rest_framework import serializers

from apps.measurement.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Currency
        fields = ['currency', 'code', 'numeric', 'digit', 'country']


class CurrencyBriefSerializer(serializers.ModelSerializer):
    """"""
    name = serializers.CharField(source='currency')

    class Meta:
        model = Currency
        fields: tuple = (
            'name',
            'code',
        )
