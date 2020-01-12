from rest_framework.views import APIView
from event_management.serializers import VenueCreateSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from event_management.models import Venue
from settings.models import Address
from helpers.functions import json_formatter
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class VenueCreateView(APIView):
    """
    Create new venue

    Url: /api/event/venue/create/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = VenueCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = VenueCreateSerializer(data=data)

        if serializer.is_valid():
            json_data = {'form': 'valid'}
            address_serializer = serializer.validated_data['address_serializer']
            address = address_serializer.get('address')
            latitude = address_serializer.get('latitude')
            longitude = address_serializer.get('longitude')

            address_obj = Address.objects.create(address=address, latitude=latitude, longitude=longitude)

            address_fields = ['address', 'latitude', 'longitude']
            json_data.update({'address': json_formatter(data_obj=address_obj, fields=address_fields)})

            amenities = serializer.validated_data['amenities']
            capacity = serializer.validated_data['capacity']
            contact_person = serializer.validated_data['contact_person']
            contact_mobile = serializer.validated_data['contact_mobile']

            venue_obj = Venue.objects.create(address=address_obj, amenities=amenities, capacity=capacity,
                                             contact_person=contact_person, contact_mobile=contact_mobile)

            venue_fields = ['amenities', 'capacity', 'contact_person', 'contact_mobile']
            json_data.update({'venue': json_formatter(data_obj=venue_obj, fields=venue_fields)})
            status = HTTP_200_OK
        else:
            json_data = {'form': 'invalid'}
            json_data.update({'address': None, 'venue': None})
            status = HTTP_400_BAD_REQUEST

        return Response(json_data, status=status)
