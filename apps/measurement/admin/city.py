from django.contrib.gis import admin

from apps.measurement.models import City
from apps.utils.admin import TimeStampAdminMixin


class CityInline(admin.StackedInline):
    model = City
    verbose_name_plural = 'Cities'


@admin.register(City)
class CityAdmin(TimeStampAdminMixin):
    list_display: list = [
        'id',
        'name',
    ] + TimeStampAdminMixin.list_display
