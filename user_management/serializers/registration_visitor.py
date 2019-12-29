from rest_framework import serializers
from user_management.models import User, VisitorProfile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class VisitorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorProfile
        exclude = ('user',)


class VisitorRegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, label='Confirm Password')
    visitor_profile = VisitorProfileSerializer()

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'password_confirmation', 'visitor_profile')

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def validate(self, data):
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password not in ['', None] and password_confirmation not in ['', None]:
            if password != password_confirmation:
                raise serializers.ValidationError('Password and Password confirmation do not match')
            return data
        raise data
    #
    # def create(self, validated_data):
    #     ingredients_data = validated_data.pop('visitor_profile')
    #     recipe = User.objects.create(**validated_data)
    #
    #     for ingredient in ingredients_data:
    #         ingredient, created = VisitorProfile.objects.get_or_create(name=ingredient['name'])
    #         recipe.visitorprofile.add(ingredient)
    #     return recipe

