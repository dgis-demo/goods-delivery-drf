import collections

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.notifications.tasks import send_push_notifications
from apps.notifications.validators import push_template_validator


class PushTemplate(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    template = models.TextField(verbose_name=_('template'), validators=[push_template_validator], help_text=_(
        'Please, use the following template as example: '
        '<b>Order {order_id} for {order_sum}{order_currency} is {order_status}.<b/>'
    ))
    template_pl = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'push_template'

        verbose_name = _('push notification template')
        verbose_name_plural = _('push notification templates')

    def __str__(self) -> str:
        return str(self.name)

    def get_push_content(self, **kwargs) -> str:
        mapping = collections.defaultdict(str)
        mapping.update(kwargs)
        return str(self.template).format_map(mapping)

    def send_push_notifications(self, user: get_user_model(), **kwargs):
        if user.tokens:
            body = self.get_push_content(**kwargs)
            send_push_notifications.delay(user.tokens, self.name, body)
