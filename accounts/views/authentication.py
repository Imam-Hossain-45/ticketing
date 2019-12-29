from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as auth_logout
from accounts.serializers import UserLogInSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from accounts.helpers import my_login


class UserLogInView(APIView):
    """
    Show a login form to log a user in.

    Url: /accounts/login/
    """

    permission_classes = [AllowAny]
    serializer_class = UserLogInSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLogInSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            username = request.data['username']
            password = request.data['password']
            json_data, status = my_login(self=self, username=username, password=password, data=data)
            return Response(json_data, status)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogOutView(LoginRequiredMixin, APIView):
    """
    Log a user out.

    Url: /accounts/logout/
    """

    def post(self, request, *args, **kwargs):
        auth_logout(self.request)
        return Response(status=HTTP_200_OK)
