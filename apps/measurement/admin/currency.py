from django.contrib.gis import admin

from apps.measurement.models import Currency
from apps.utils.admin import TimeStampAdminMixin


class CurrencyInline(admin.StackedInline):
    model = Currency
    verbose_name_plural = 'Currencies'
    extra = 1
    max_num = 1


@admin.register(Currency)
class CurrencyAdmin(TimeStampAdminMixin):
    list_display = [
        'id', 'currency', 'code',
        'numeric', 'digit'
    ] + TimeStampAdminMixin.list_display
