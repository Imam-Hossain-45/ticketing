from rest_framework import serializers
from event_management.models import Event
from settings.models import Preference


class EventCreateSerializer(serializers.ModelSerializer):
    try:
        choices = [(pref.id, pref.caption) for pref in Preference.objects.all()]
    except:
        choices = []
    preferences = serializers.MultipleChoiceField(choices=choices)

    class Meta:
        model = Event
        fields = ('title', 'description', 'banner', 'start_date', 'end_date', 'start_time', 'end_time', 'open_gallery',
                  'seat_range', 'paid', 'cost', 'preferences', 'venue', 'organizer', 'instruction')
