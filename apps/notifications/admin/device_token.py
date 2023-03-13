from django.contrib import admin

from apps.notifications.models import DeviceToken
from apps.utils.admin import TimeStampAdminMixin


@admin.register(DeviceToken)
class DeviceTokenAdmin(TimeStampAdminMixin):
    list_display = [
       'id', 'user', 'token', 'device', 'device_id', 'device_type', 'is_enabled'
    ] + TimeStampAdminMixin.list_display
