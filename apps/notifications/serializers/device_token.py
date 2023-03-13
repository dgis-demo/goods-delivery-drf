from rest_framework import serializers

from apps.notifications.models import DeviceToken


class DeviceTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceToken
        fields = ['id', 'device_id', 'device_type', 'token']
