from helpers.models import Model
from django.db import models


class Ticket(Model):
    user = models.ForeignKey('user_management.User', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey('event_management.Event', on_delete=models.CASCADE)
    serial_no = models.CharField(max_length=20)
    seat_no = models.CharField(max_length=10)
    is_valid = models.BooleanField(default=True, blank=True)
    used = models.BooleanField(default=False, blank=True)
