from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as auth_logout
from accounts.serializers import UserLogInSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from accounts.helpers import get_user_json
from django.middleware.csrf import get_token


class UserLogInView(APIView):
    """
    Show a login form to log a user in.

    Url: /accounts/login/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserLogInSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = UserLogInSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            json_data, status = get_user_json(self=self, valid=True, username=username, password=password)

        else:
            json_data, status = get_user_json(self=self, valid=False, error=serializer.errors)

        return Response(json_data, status)


class LogOutView(LoginRequiredMixin, APIView):
    """
    Log a user out.

    Url: /accounts/logout/
    """

    def post(self, request, *args, **kwargs):
        auth_logout(self.request)
        return Response(status=HTTP_200_OK)
