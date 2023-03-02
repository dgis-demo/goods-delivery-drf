from django.contrib.gis import admin

from apps.measurement.models import Country
from apps.utils.admin import TimeStampAdminMixin

from .city import CityInline
from .currency import CurrencyInline


@admin.register(Country)
class CountryAdmin(TimeStampAdminMixin):
    list_display = [
        'id', 'full_name', 'short_name',
        'alpha2', 'alpha3', 'code'
    ] + TimeStampAdminMixin.list_display

    inlines: tuple = (
        CityInline,
        CurrencyInline,
    )
