from rest_framework import serializers
from user_management.models import VisitorProfile


class ChangeProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorProfile
        fields = ('profile_picture', )
