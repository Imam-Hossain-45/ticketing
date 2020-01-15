from django.contrib import admin
from event_management.models import Event, Venue, EventPreference

# Register your models here.

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(EventPreference)
