from rest_framework import serializers
from dh_test.models import AndroidTestUser


class ScanQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidTestUser
        fields = ('ticket_id', )
