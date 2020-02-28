from rest_framework import serializers
from dh_test.models import UserRegistration


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
