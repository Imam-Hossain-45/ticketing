from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from settings.models import Preference
from rest_framework.status import HTTP_200_OK
from django.core import serializers
import json


class GetAllPreferencesView(APIView):
    """
    get all the preferences

    Url: /settings/get-preferences/
    """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        preferences = Preference.objects.all()
        fields = ['id', 'caption']
        json_data = {}
        # json_data.update({'size': preferences.count()})
        for preference in preferences:
            key = preference.id
            data = json_formatter(data_obj=preference, fields=fields)
            if not data['id']:
                data['id'] = key
            json_data.update({key: data})

        return Response(json_data, status=HTTP_200_OK)


def json_formatter(data_obj=None, fields=None):
    data = json.loads(
        serializers.serialize('json', [data_obj], fields=fields)
    )[0]
    formatted_data = {field: data['fields'].get(field) for field in fields}
    return formatted_data
