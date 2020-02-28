from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from dh_test.models import Country, UserRegistration, FnF, FoodPreference, LanguageProficiency
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.conf import settings


class GetCountryView(APIView):
    """
    get all the countries

    Url: /api/test/web/get-countries/
    """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        countries = Country.objects.all()
        data_list = []
        for country in countries:
            data_list.append({
                'id': country.id,
                'code': country.code,
                'name': country.name,
                'dial_code': country.dial_code,
                'currency': country.currency
            })

        return Response(data_list, status=HTTP_200_OK)


class RegistrationListView(APIView):
    """
        get all the registrations list

        Url: /api/test/web/registration/list/
        """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        registrations = UserRegistration.objects.all()
        data_list = []
        for registration in registrations:
            data_list.append({
                'id': registration.id,
                'name': registration.name,
                'mobile_number': registration.mobile_number,
                'date_of_registration': registration.created_at,
                'profile_picture1': settings.MEDIA_URL_HEADER + str(
                    registration.profile_picture1) if registration.profile_picture1 not in ['', None] else None,
                'profile_picture2': settings.MEDIA_URL_HEADER + str(
                    registration.profile_picture2) if registration.profile_picture2 not in ['', None] else None
            })

        return Response(data_list, status=HTTP_200_OK)


class RegistrationDetailView(APIView):
    """
        get registration detail

        Url: /api/test/web/registration/<registration_id>/detail/
        """

    permission_classes = [AllowAny]

    def get(self, request, format=None, **kwargs):
        registration_id = self.kwargs.get('registration_id', None)
        if not registration_id.isdigit():
            return Response({'request': 'invalid, improper registration id provided'}, status=HTTP_400_BAD_REQUEST)
        try:
            registration = UserRegistration.objects.get(id=registration_id)

            fnfs_qs = FnF.objects.filter(user_registration=registration)
            fnf_data_list = []
            for fnf in fnfs_qs:
                fnf_data_list.append({
                    'name': fnf.name,
                    'date_of_birth': fnf.date_of_birth,
                    'gender': fnf.gender,
                    'mobile_number': fnf.mobile_number
                })

            food_preferences_qs = FoodPreference.objects.filter(user_registration=registration)
            food_preference_data_list = []
            for food_preference in food_preferences_qs:
                food_preference_data_list.append(
                    food_preference.food
                )

            language_proficiency_qs = LanguageProficiency.objects.filter(user_registration=registration)
            language_proficiency_list = []
            for language_proficiency in language_proficiency_qs:
                language_proficiency_list.append({
                    'language': language_proficiency.language,
                    'level': language_proficiency.level
                })

            json_data = {
                'name': registration.name,
                'date_of_birth': registration.date_of_birth,
                'gender': registration.gender,
                'mobile_number': registration.mobile_number,
                'email': registration.email,
                'country': registration.country.name,
                'profile_picture1': settings.MEDIA_URL_HEADER + str(
                    registration.profile_picture1) if registration.profile_picture1 not in ['', None] else None,
                'profile_picture2': settings.MEDIA_URL_HEADER + str(
                    registration.profile_picture2) if registration.profile_picture2 not in ['', None] else None,
                'fnfs': fnf_data_list,
                'food_preferences': food_preference_data_list,
                'language_proficiencies': language_proficiency_list
            }

            return Response(json_data, status=HTTP_200_OK)

        except:
            return Response({'request': 'invalid, wrong registration id provided'}, status=HTTP_404_NOT_FOUND)
