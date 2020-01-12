from rest_framework import serializers
from event_management.models import Event
from settings.models import Preference


class EventCreateSerializer(serializers.ModelSerializer):
    preferences = serializers.MultipleChoiceField(
        choices=[(pref.id, pref.caption) for pref in Preference.objects.all()]
    )

    class Meta:
        model = Event
        fields = ('title', 'description', 'banner', 'start_date', 'end_date', 'start_time', 'end_time', 'open_gallery',
                  'seat_range', 'paid', 'cost', 'preferences', 'venue', 'organizer', 'instruction')
