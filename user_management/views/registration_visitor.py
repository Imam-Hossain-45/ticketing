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
        data = request.data
        serializer = VisitorRegistrationSerializer(data=data)
        print(request.data)

        if serializer.is_valid(raise_exception=True):
            email = request.data['email']
            phone = request.data['phone']
            password = request.data['password']
            # user = serializer.save(commit=False)
            # user = User.objects.create(email=email, phone=phone)
            print(serializer.validate_password(password))
            #
            # try:
            #     validate_password(password, user)
            # except ValidationError as e:
            #     user.delete()
            #     data['error'] = e
            #     return Response(data, status=HTTP_400_BAD_REQUEST)
        #     username = request.data['username']
        #     password = request.data['password']
        #     json_data, status = my_login(self=self, username=username, password=password, data=data)
        #     return Response(json_data, status)

        return Response(data, status=HTTP_400_BAD_REQUEST)