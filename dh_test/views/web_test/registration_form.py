from rest_framework.views import APIView
from dh_test.models import UserRegistration, FnF, FoodPreference, LanguageProficiency
from dh_test.serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class UserRegistrationView(APIView):
    """
    User registration
    Url: /api/test/web/user-event/registration/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = UserRegistrationSerializer(data=data)

        if serializer.is_valid() and 'fnfs' in data and 'food_preferences' in data and 'language_proficiencies' in data:
            name = serializer.validated_data['name']
            date_of_birth = serializer.validated_data['date_of_birth']
            gender = serializer.validated_data['gender']
            mobile_number = serializer.validated_data['mobile_number']
            email = serializer.validated_data['email']
            country = serializer.validated_data['country']
            profile_picture1 = serializer.validated_data['profile_picture1']
            profile_picture2 = serializer.validated_data['profile_picture2']

            registration = UserRegistration.objects.create(
                name=name, date_of_birth=date_of_birth, gender=gender, mobile_number=mobile_number,
                email=email, country=country, profile_picture1=profile_picture1, profile_picture2=profile_picture2
            )

            try:
                fnfs = data['fnfs']
                for fnf in fnfs:
                    fnf_name = fnf['name']
                    fnf_date_of_birth = fnf['date_of_birth']
                    fnf_gender = fnf['gender']
                    fnf_mobile_number = fnf['mobile_number']
                    FnF.objects.create(
                        user_registration=registration, name=fnf_name, date_of_birth=fnf_date_of_birth,
                        gender=fnf_gender, mobile_number=fnf_mobile_number
                    )

                food_preferences = data['food_preferences']
                for food in food_preferences:
                    FoodPreference.objects.create(
                        user_registration=registration, food=food
                    )

                language_proficiencies = data['language_proficiencies']
                for language_proficiency in language_proficiencies:
                    language = language_proficiency['language']
                    level = language_proficiency['level']
                    LanguageProficiency.objects.create(
                        user_registration=registration, language=language, level=level
                    )
                json_data = {'registration': 'valid'}
                status = HTTP_200_OK

            except Exception as e:
                registration.delete()
                json_data = {'registration': 'invalid', 'errors': e}
                status = HTTP_400_BAD_REQUEST

        else:
            json_data = {'registration': 'invalid', 'errors': serializer.errors}
            status = HTTP_400_BAD_REQUEST

        return Response(json_data, status=status)

