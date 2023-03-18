from uuid import uuid4

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from . import exceptions
from .models import User
from .validatiors import phone_validator


class UserCodeVerifySerializer(serializers.ModelSerializer):
    otp_code = serializers.CharField(min_length=4, max_length=4, write_only=True, required=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['phone', 'otp_code', 'access', 'refresh']
        extra_kwargs = {
            'phone': {'allow_blank': False, 'required': True, 'validators': [phone_validator], 'write_only': True}
        }

    def validate(self, data):
        default_validation_error = serializers.ValidationError({'phone': [_('Phone or otp is incorrect')]})
        try:
            user = User.objects.get(phone=data['phone'])
            self.context['request'].log_context['phone'] = data['phone']
            if not user.is_active:
                raise serializers.ValidationError({'phone': [_('User is blocked')]})
        except User.DoesNotExist as e:
            raise default_validation_error from e
        try:
            otp = user.check_otp(data['otp_code'])
        except exceptions.InvalidCodeException as e:
            raise default_validation_error from e
        data['debug'] = otp.debug_dict
        if not otp.check_success:
            raise default_validation_error
        token = RefreshToken.for_user(user)
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
        return data

    @property
    def data(self):
        data = super().data
        if self.validated_data.get('debug'):
            data['debug'] = self.validated_data.get('debug')
        return data


class UserLoginPhoneSerializer(serializers.ModelSerializer):
    resend_time = serializers.IntegerField(read_only=True)
    is_new_user = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['phone', 'resend_time', 'is_new_user']
        extra_kwargs = {
            'phone': {'allow_blank': False, 'required': True, 'validators': [phone_validator], 'write_only': True}
        }
        ref_name = 'Request OTP'

    def validate(self, data):
        try:
            is_new_user = False
            user = User.objects.get(phone=data['phone'])
            if not user.is_active:
                raise serializers.ValidationError({'phone': [_('User is blocked')]})
        except User.DoesNotExist:
            user = User.objects.create(
                username=uuid4().hex[:30],
                phone=data['phone'],
                role=self.context.get('role'),
            )
            is_new_user = True

        data['user'] = user
        data['is_new_user'] = is_new_user
        otp = user.send_otp()
        data['debug'] = otp.debug_dict
        data['resend_time'] = otp.resend_time
        return data

    @property
    def data(self):
        data = super().data
        if self.validated_data.get('debug'):
            data['debug'] = self.validated_data.get('debug')
        return data


class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name']
