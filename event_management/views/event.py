from rest_framework.views import APIView
from event_management.serializers import EventCreateSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from event_management.models import Event, EventPreference
from settings.models import Preference
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_406_NOT_ACCEPTABLE
from helpers.functions import json_formatter
from decimal import Decimal
from django.conf import settings


class EventCreateView(APIView):
    """
    Create new event

    Url: /api/event/create/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = EventCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = EventCreateSerializer(data=data)

        if serializer.is_valid():
            try:
                seat_range = serializer.validated_data['seat_range']
            except:
                return Response({'form': 'invalid',
                                 'error': {
                                     'seat_range': ['invalid input']
                                 }
                                 },
                                status=HTTP_400_BAD_REQUEST)
            try:
                cost = serializer.validated_data['cost']
            except:
                return Response({'form': 'invalid',
                                 'error': {
                                     'cost': ['invalid input']
                                 }
                                 },
                                status=HTTP_400_BAD_REQUEST)

            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            if start_date > end_date:
                return Response({'form': 'invalid',
                                 'error': {
                                     'end_date': ['end date cannot be less than start date']
                                 }
                                 },
                                status=HTTP_406_NOT_ACCEPTABLE)

            title = serializer.validated_data['title']
            description = serializer.validated_data['description']
            banner = serializer.validated_data['banner']
            start_time = serializer.validated_data['start_time']
            end_time = serializer.validated_data['end_time']
            open_gallery = serializer.validated_data['open_gallery']
            paid = serializer.validated_data['paid']
            venue = serializer.validated_data['venue']
            organizer = serializer.validated_data['organizer']
            instruction = serializer.validated_data['instruction']

            if request.user.is_authenticated:
                created_by = request.user
                updated_by = request.user
            else:
                created_by = None
                updated_by = None

            event_obj = Event.objects.create(
                title=title, description=description, banner=banner, start_date=start_date, end_date=end_date,
                start_time=start_time, end_time=end_time, open_gallery=open_gallery, seat_range=seat_range,
                paid=paid, cost=cost, venue=venue, organizer=organizer, instruction=instruction, created_by=created_by,
                updated_by=updated_by
            )

            preference_list = []
            for list_no, preference in enumerate(data.getlist('preferences')):
                preference_obj = Preference.objects.get(id=preference)
                preference_list.append(str(preference_obj))
                EventPreference.objects.create(
                    event=event_obj,
                    preference=preference_obj
                )

            json_data = {'form': 'valid'}
            event_fields = ['title', 'description', 'start_date', 'end_date', 'start_time', 'end_time', 'open_gallery',
                            'seat_range', 'paid', 'organizer', 'instruction', 'created_by', 'updated_by']
            json_data.update(json_formatter(data_obj=event_obj, fields=event_fields))
            json_data.update({'cost': Decimal(event_obj.cost)})

            json_data.update({'venue': str(venue)})
            json_data.update({'banner': '{}{}'.format(settings.MEDIA_URL_HEADER, event_obj.banner)})
            json_data.update({'preferences': preference_list})

            status = HTTP_200_OK

        else:
            json_data = {'form': 'invalid', 'error': serializer.errors}
            status = HTTP_400_BAD_REQUEST

        return Response(json_data, status=status)


class EventListAllView(APIView):
    """
        get all the events list

        Url: /api/event/get-all-list/
        """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        events = Event.objects.all()
        data_list = []
        for event in events:
            preference_list = []
            event_preferences_qs = EventPreference.objects.filter(event=event)
            for event_preference in event_preferences_qs:
                preference_list.append(str(event_preference.preference))
            data_list.append(
                {
                    'id': event.id,
                    'title': event.title,
                    'description': event.description,
                    'start_date': event.start_date,
                    'end_date': event.end_date,
                    'start_time': event.start_time,
                    'end_time': event.end_time,
                    'open_gallery': event.open_gallery,
                    'seat_range': event.seat_range,
                    'paid': event.paid,
                    'cost': event.cost,
                    'venue': str(event.venue),
                    'preferences': preference_list,
                    'organizer': event.organizer,
                    'instruction': event.instruction,
                    'created_by': event.created_by,
                    'updated_by': event.updated_by,
                }
            )

        return Response(data_list, status=HTTP_200_OK)
