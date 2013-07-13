from django.db import models
from django.utils.translation import ugettext_lazy as _


class BookingTypes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        db_table = 'booking_types'
        verbose_name = _('BookingType')
        verbose_name_plural = _('BookingTypes')