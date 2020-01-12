from rest_framework import serializers
from event_management.models import Venue
from settings.models import Address


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class VenueCreateSerializer(serializers.ModelSerializer):
    address = AddressCreateSerializer()

    class Meta:
        model = Venue
        fields = ('address', 'amenities', 'capacity', 'contact_person', 'contact_mobile')
