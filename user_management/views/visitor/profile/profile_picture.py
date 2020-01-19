from rest_framework.views import APIView
from user_management.serializers import ChangeProfilePictureSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user_management.models import User, VisitorProfile
from django.conf import settings
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class ChangeProfilePictureView(APIView):
    """
    Change profile picture of a registered visitor user

    Url: /api/user/visitor/<user_id>/profile/change-profile-picture/
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ChangeProfilePictureSerializer

    def post(self, request, *args, **kwargs):
        request_key = 'request'
        profile_picture_key = 'profile_picture'
        message_key = 'message'
        invalid_request_value = 'invalid'
        invalid_profile_picture_value = ''
        invalid_status = HTTP_400_BAD_REQUEST
        valid_status = HTTP_200_OK

        invalid_json_data = {
            request_key: invalid_request_value,
            profile_picture_key: invalid_profile_picture_value
        }

        url_user_id = self.kwargs.get('user_id', None)
        if not url_user_id.isdigit():
            invalid_json_data.update({message_key: 'invalid url provided'})
            return Response(invalid_json_data, invalid_status)
        data = request.data.copy()
        serializer = ChangeProfilePictureSerializer(data=data)

        # print(type(request.user))

        if serializer.is_valid():
            # data['user_id'] = 2
            if 'user_id' not in data:
                invalid_json_data.update({message_key: 'no user-id provided to change profile picture'})
                return Response(invalid_json_data, invalid_status)

            user_id = data['user_id']
            if not type(user_id) == str or not user_id.isdigit():
                invalid_json_data.update({message_key: 'invalid user-id type'})
                return Response(invalid_json_data, invalid_status)

            user_id = int(user_id)
            if user_id < 1:
                invalid_json_data.update({message_key: 'invalid user-id provided'})
                return Response(invalid_json_data, invalid_status)

            profile_picture = serializer.validated_data['profile_picture']
            # if request.user.id == url_user_id:
            if profile_picture:
                if user_id == int(url_user_id):
                    try:
                        user = User.objects.get(id=user_id)
                    except:
                        invalid_json_data.update({message_key: 'invalid user-id provided'})
                        return Response(invalid_json_data, invalid_status)
                    try:
                        VisitorProfile.objects.get(user=user)
                    except:
                        invalid_json_data.update({message_key: 'user is not a visitor type'})
                        return Response(invalid_json_data, invalid_status)

                    user.visitorprofile.profile_picture = profile_picture
                    user.visitorprofile.save()

                    valid_json_data = {
                        request_key: 'valid',
                        profile_picture_key: '{}{}'.format(settings.MEDIA_URL_HEADER,
                                                           user.visitorprofile.profile_picture),
                        message_key: 'profile picture updated'
                    }
                    return Response(valid_json_data, valid_status)

                else:
                    invalid_json_data.update({message_key: 'forbidden user: user not allowed'})

        else:
            invalid_json_data.update({message_key: 'invalid data input'})

        return Response(invalid_json_data, invalid_status)
