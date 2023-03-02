from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import TimeStampModelMixin

from .country import Country


class City(TimeStampModelMixin):
    """"""

    name = models.CharField(
        verbose_name=_('name'),
        max_length=128,
        unique=True
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cities',
        verbose_name=_('country')
    )

    class Meta:
        """"""
        db_table = 'city'

        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self) -> str:
        """"""
        return f"{self.name}"
