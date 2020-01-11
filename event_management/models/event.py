from helpers.models import Model
from django.db import models


class Event(Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    open_gallery = models.BooleanField(default=True, blank=True)
    seat_range = models.IntegerField(default=-1, blank=True)
    paid = models.BooleanField(default=False, blank=True)
    cost = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    preference = models.ManyToManyField('settings.Preference', through='event_management.EventPreference')
    venue = models.ForeignKey('event_management.Venue', on_delete=models.SET_NULL, null=True)
    organizer = models.CharField(max_length=60)
    instruction = models.TextField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('user_management.User', related_name='created_by',
                                   on_delete=models.SET_NULL, blank=True, null=True)
    updated_by = models.ForeignKey('user_management.User', related_name='updated_by',
                                   on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


class EventPreference(Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    preference = models.ForeignKey('settings.Preference', on_delete=models.CASCADE)
