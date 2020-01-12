from helpers.models import Model
from django.db import models


class Address(Model):
    address = models.TextField(max_length=128)
    # country = models.CharField()
    # city = models.CharField()
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=False, null=False)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.address)
