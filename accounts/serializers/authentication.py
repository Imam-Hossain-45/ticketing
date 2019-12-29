from rest_framework import serializers


class UserLogInSerializer(serializers.Serializer):
    """Login Serializer."""

    username = serializers.CharField(label='Username')
    password = serializers.CharField(label='Password')

    # def validate(self, data):
    #     phone = data['phone']
    #     if phone in ['', None]:
    #         raise serializers.ValidationError('Phone Field is required')
    #     return data
