from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel
from locations.models import Location


class Consumption(BaseModel):
    timestamp = models.DateTimeField(_("timestamp"))
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(_("value"))

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "location"], name="unique_consumption",
            )
        ]
        verbose_name = _("consumption")
        verbose_name_plural = _("consumptions")
