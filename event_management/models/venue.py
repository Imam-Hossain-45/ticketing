from helpers.models import Model
from django.db import models


class Venue(Model):
    address = models.ForeignKey('settings.Address', on_delete=models.SET_NULL, null=True)
    amenities = models.TextField()
    capacity = models.IntegerField()
    contact_person = models.CharField(max_length=40)
    contact_mobile = models.CharField(max_length=11)
