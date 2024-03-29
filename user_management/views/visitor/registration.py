from rest_framework.views import APIView
from user_management.serializers import VisitorRegistrationSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user_management.models import User, VisitorProfile, UserAuthority
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from accounts.helpers import get_user_json
from rest_framework.status import HTTP_400_BAD_REQUEST


class VisitorRegistrationView(APIView):
    """
    Register a visitor and login the user

    Url: /api/user/visitor/create/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = VisitorRegistrationSerializer

    # def get(self, request, format=None, **kwargs):
    #     # cart = get_cart(request)
    #     cart_serializer = self.serializer_class()
    #     another_serializer = self.visitor_profile_serializer_class()
    #
    #     return Response({
    #         'cart': cart_serializer.data,
    #         'another': another_serializer.data,
    #     })

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = VisitorRegistrationSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']

            try:
                user_type = UserAuthority.objects.get(user_type='visitor')
            except:
                return Response({'valid_credential': 'invalid',
                                 'response': {
                                     "user_type": [
                                         "user type does not exist."
                                     ]
                                 }
                                 }, status=HTTP_400_BAD_REQUEST)

            # equivalent to user.save(commit=False)
            user = User(username=username, email=email, phone=phone, phone_verified=True, user_type=user_type)

            try:
                validate_password(password, user)
            except ValidationError as e:
                json_data, status = get_user_json(self=self, valid=False, error={'password': e})
                return Response(json_data, status)
            user.set_password(password)
            user.save()

            visitor_profile = serializer.validated_data['visitor_profile']
            first_name = visitor_profile.get('first_name')
            last_name = visitor_profile.get('last_name')
            gender = visitor_profile.get('gender')
            date_of_birth = visitor_profile.get('date_of_birth')
            profile_picture = visitor_profile.get('profile_picture')

            VisitorProfile.objects.create(
                user=user, first_name=first_name, last_name=last_name, gender=gender, date_of_birth=date_of_birth,
                profile_picture=profile_picture
            )
            json_data, status = get_user_json(
                self=self, valid=True, username=username, password=password, success_message='Successfully Signed Up'
            )

        else:
            json_data, status = get_user_json(self=self, valid=False, error=serializer.errors)
            if 'non_field_errors' in json_data['response']:
                json_data['response'].update({'password': json_data['response']['non_field_errors']})
                del json_data['response']['non_field_errors']

        return Response(json_data, status)
