from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModelMixin(models.Model):
    """The fields `created_at` and `updated_at` are added."""

    created_at = models.DateTimeField(
        verbose_name=_("created date"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated date"),
        auto_now=True
    )

    class Meta:
        abstract = True
