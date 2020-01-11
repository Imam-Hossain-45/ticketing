from django.db import models
from helpers.models import Model
from settings.models import SERVICE_CHOICES


class BusinessProfile(Model):
    email = models.EmailField()
    name = models.CharField(max_length=60)
    address = models.ForeignKey('settings.Address', on_delete=models.SET_NULL, null=True)
    service = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        default='venue-event'
    )
    contact_person = models.CharField(max_length=40)
    contact_mobile = models.CharField(max_length=11)
    logo = models.ImageField(upload_to='user_business/logo/', null=True, blank=True)

