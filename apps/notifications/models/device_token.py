from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import TimeStampModelMixin


class DeviceToken(TimeStampModelMixin):
    class DeviceType(models.TextChoices):
        IOS = 'IOS', 'IOS'
        ANDROID = 'ANDROID', 'Android'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='device_tokens',
                             verbose_name=_('user'))
    token = models.CharField(max_length=255, verbose_name=_('token'))
    device = models.JSONField(verbose_name=_('device'), blank=True, null=True)
    device_id = models.CharField(max_length=50, verbose_name=_('device ID'))
    device_type = models.CharField(max_length=10, choices=DeviceType.choices, verbose_name=_('device type'))
    is_enabled = models.BooleanField(default=True, verbose_name=_('is enabled'))

    class Meta:
        db_table = 'device_token'

        verbose_name = _('device token')
        verbose_name_plural = _('device tokens')

    def __str__(self) -> str:
        return str(self.token)
