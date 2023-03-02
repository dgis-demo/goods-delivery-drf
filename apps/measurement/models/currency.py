from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import TimeStampModelMixin

from .country import Country


class Currency(TimeStampModelMixin):
    """
        Active ISO 4217 currency codes
        https://en.wikipedia.org/wiki/ISO_4217
    """

    currency = models.CharField(
        verbose_name=_('full name'),
        max_length=128,
        unique=True
    )
    code = models.CharField(
        verbose_name=_('alphabetic code'),
        max_length=3,
    )
    numeric = models.CharField(
        verbose_name=_('numeric code'),
        max_length=3,
        blank=True,
        null=True
    )
    digit = models.CharField(
        verbose_name=_('minor unit'),
        max_length=8,
        blank=True,
        null=True
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='currencies',
        verbose_name=_('country')
    )

    class Meta:
        """"""
        db_table = 'currency'

        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

        ordering = ('code', )

    def __str__(self) -> str:
        """"""
        return f"{self.code}-{self.currency}"
