from rest_framework import serializers


class UserLogInSerializer(serializers.Serializer):
    """Login Serializer."""

    username = serializers.CharField(label='Username')
    password = serializers.CharField(style={'input_type': 'password'}, label='Password')

