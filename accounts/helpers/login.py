from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from user_management.models import User, VisitorProfile
from django.core import serializers
from django.contrib.auth import login, authenticate
import json
from django.conf import settings


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


def get_user_json(self=None, valid=None, username=None, password=None, error=None, success_message=None):
    fields = ['email', 'phone', 'user_type', 'status']
    profile_fields = [field.name for field in VisitorProfile._meta.fields]

    if valid:
        user = my_authenticate(username=username, password=password)
        if user and user.is_active:
            status = HTTP_200_OK
            login(self.request, user)

            json_data = {'valid_credential': 'valid'}
            json_data.update({'response': success_message})
            json_data.update(my_json_formatter(fields=fields, data_obj=user))

            if VisitorProfile.objects.filter(user=user).exists():
                json_data.update({'user_profile_data_exist': True})
                profile = VisitorProfile.objects.get(user=user)
                json_data.update(my_json_formatter(fields=profile_fields, data_obj=profile))

                if json_data['profile_picture'] == '':
                    json_data['profile_picture'] = None
                else:
                    json_data['profile_picture'] = settings.MEDIA_URL_HEADER + json_data['profile_picture']
            else:
                json_data.update({'user_profile_data_exist': False})
                json_data.update(my_json_formatter(fields=profile_fields))

        else:
            status = HTTP_404_NOT_FOUND
            json_data = {'valid_credential': 'invalid'}
            json_data.update({'response': 'username or password invalid'})
            json_data.update(my_json_formatter(fields=fields))
            json_data.update({'user_profile_data_exist': False})
            json_data.update(my_json_formatter(fields=profile_fields))
    else:
        status = HTTP_400_BAD_REQUEST
        json_data = {'valid_credential': 'invalid'}
        json_data.update({'response': error})
        json_data.update(my_json_formatter(fields=fields))
        json_data.update({'user_profile_data_exist': False})
        json_data.update(my_json_formatter(fields=profile_fields))

    return json_data, status


def my_json_formatter(fields=None, data_obj=None):
    if fields:
        if data_obj:
            data = json.loads(
                serializers.serialize('json', [data_obj], fields=fields)
            )[0]
            formatted_data = {field: data['fields'].get(field) for field in fields if not field.startswith('_')}
        else:
            formatted_data = {field: None for field in fields}
    else:
        formatted_data = None
    return formatted_data
