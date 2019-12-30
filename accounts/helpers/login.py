from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from user_management.models import User, VisitorProfile
from django.core import serializers
from django.contrib.auth import login, authenticate
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


def my_login(self, username, password, data):
    user = my_authenticate(username=username, password=password)
    if user and user.is_active:
        login(self.request, user)
        fields = ['email', 'phone', 'user_type', 'is_active']
        user_data = json.loads(
            serializers.serialize('json', [user], fields=fields)
        )[0]

        json_data = {f: user_data['fields'].get(f) for f in fields}
        # json_data = user_data
        if VisitorProfile.objects.filter(user=user).exists():
            json_data['user_profile_data_exist'] = True
            profile = VisitorProfile.objects.get(user=user)
            user_profile_data = json.loads(serializers.serialize('json', [profile, ]))[0]
            user_profile_data_dict = {f: user_profile_data['fields'].get(f) for f in vars(profile) if not f.startswith('_') and 'id' not in f}
            print(user_profile_data_dict)
            json_data.update(user_profile_data_dict)
        else:
            json_data['user_profile_data_exist'] = False
        return json_data, HTTP_200_OK
    return data, HTTP_404_NOT_FOUND

