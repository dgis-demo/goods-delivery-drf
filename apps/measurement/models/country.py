from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import TimeStampModelMixin


class Country(TimeStampModelMixin):
    """
        Officially assigned code elements
        https://en.wikipedia.org/wiki/ISO_3166-1
    """

    full_name = models.CharField(
        verbose_name=_('full name'),
        max_length=128,
        unique=True
    )
    short_name = models.CharField(
        verbose_name=_('short name'),
        max_length=64,
        unique=True
    )
    alpha2 = models.CharField(
        verbose_name=_('alpha-2 code'),
        max_length=2,
        blank=True,
        null=True
    )
    alpha3 = models.CharField(
        verbose_name=_('alpha-3 code'),
        max_length=3,
        blank=True,
        null=True
    )
    code = models.CharField(
        verbose_name=_('numeric code'),
        max_length=3,
        blank=True,
        null=True
    )

    class Meta:
        """"""
        db_table = 'country'

        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

        ordering = ('alpha3', )

    def __str__(self) -> str:
        """"""
        return f"{self.alpha3}-{self.full_name}"
