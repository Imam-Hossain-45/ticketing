from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout as auth_logout
from accounts.serializers import UserLogInSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from user_management.models import User, VisitorProfile
from django.core import serializers
import json


def my_authenticate(username=None, password=None):
    if username:
        try:
            user = User.objects.get(email=username)
            # ====== temp ===== #
            if user:
                return None
            # ====== end temp ===== #
            return authenticate(username=username, password=password)
        except:
            try:
                user = User.objects.get(phone=username)
                if user.check_password(password):
                    return user
                return None
            except:
                return None
    return None


class UserLogInView(APIView):
    """
    Show a login form to log a user in.

    Url: /accounts/login/
    """
    # form_class = LogInForm
    permission_classes = [AllowAny]
    serializer_class = UserLogInSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLogInSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            username = request.data['username']
            password = request.data['password']

            user = my_authenticate(username=username, password=password)
            if user and user.is_active:
                login(self.request, user)
                user_data = json.loads(
                    serializers.serialize('json', [user], fields=['email', 'phone', 'user_type', 'is_active'])
                )

                json_data = {'user_data': user_data}
                if VisitorProfile.objects.filter(user=user).exists():
                    json_data['user_profile_data_exist'] = True
                    profile = VisitorProfile.objects.get(user=user)
                    user_profile_data = json.loads(serializers.serialize('json', [profile, ]))
                    json_data['user_profile_data'] = user_profile_data
                else:
                    json_data['user_profile_data_exist'] = False
                return Response(json_data, status=HTTP_200_OK)
            return Response(data, status=HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogOutView(LoginRequiredMixin, APIView):
    """
    Log a user out.

    Url: /accounts/logout/
    """

    def post(self, request, *args, **kwargs):
        auth_logout(self.request)
        return Response(status=HTTP_200_OK)
