from daterangefilter.filters import PastDateRangeFilter
from django.contrib.gis import admin


class TimeStampAdminMixin(admin.OSMGeoAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['created_at', 'updated_at']
    ordering = ('-updated_at', 'id',)
    list_filter = [
        ('created_at', PastDateRangeFilter),
    ]
