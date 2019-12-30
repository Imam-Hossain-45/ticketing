from rest_framework.views import APIView
from user_management.serializers import VisitorRegistrationSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from user_management.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class VisitorRegistrationView(APIView):
    """
    Register a visitor and login the user

    Url: /user/sign-up/
    """
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
        print(request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']
            visitor_profile = serializer.validated_data['visitor_profile']
            print(visitor_profile.get('date_of_birth'), type(visitor_profile.get('date_of_birth')))
            # user = serializer.save(commit=False)
            # print(user)
            user = User(email=email, phone=phone)
            # user.save(commit=False)
            print(user, type(user))
            # print(serializer.validate_password(password))
            #
            try:
                validate_password(password, user)
            except ValidationError as e:
                # user.delete()
                data['error'] = e
                # error = {'error': e}
                return Response(data, status=HTTP_400_BAD_REQUEST)
            user.set_password(password)
            user.save()
        #     username = request.data['username']
        #     password = request.data['password']
        #     json_data, status = my_login(self=self, username=username, password=password, data=data)
        #     return Response(json_data, status)

        return Response(data, status=HTTP_400_BAD_REQUEST)