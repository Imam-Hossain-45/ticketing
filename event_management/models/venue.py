from helpers.models import Model
from django.db import models


class Venue(Model):
    name = models.CharField(max_length=60, unique=True)
    address = models.OneToOneField('settings.Address', on_delete=models.SET_NULL, null=True)
    amenities = models.TextField()
    capacity = models.IntegerField()
    contact_person = models.CharField(max_length=40)
    contact_mobile = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.address)


# class Hall(Model):
#     venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
#     title = models.CharField(max_length=60)
#     remarks = models.TextField(max_length=128, blank=True, null=True)
