from rest_framework import serializers
from user_management.models import User, VisitorProfile


class VisitorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorProfile
        exclude = ('user',)


class VisitorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, label='Password', max_length=20)
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, label='Confirm Password')
    visitor_profile = VisitorProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'password_confirmation', 'visitor_profile')

    def validate(self, data):
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password not in ['', None] and password_confirmation not in ['', None]:
            if password != password_confirmation:
                raise serializers.ValidationError('Password and Password confirmation do not match')

        return data


class VisitorRegistrationUsernameCheckSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
