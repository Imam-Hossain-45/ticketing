from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from settings.models import Preference
from rest_framework.status import HTTP_200_OK


class PreferencesListAllView(APIView):
    """
    get all the preferences

    Url: /settings/get-preferences/
    """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        preferences = Preference.objects.all()
        data_list = []
        for preference in preferences:
            data_list.append({'id': preference.id, 'caption': preference.caption})

        # json_data = {'preferences': data_list}
        # json_data.update({'size': preferences.count()})

        return Response(data_list, status=HTTP_200_OK)

