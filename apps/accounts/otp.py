from datetime import timedelta

from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from django.utils.crypto import get_random_string

from .exceptions import InvalidCodeException, ResendNotAvailable, TemporaryBlocked
from .tasks import send_sms


class OTP:

    def __init__(self, phone):
        self.cache_exists = None
        self.phone = phone
        self.test = settings.OTP['TEST']
        self.resend_time = None
        self.check_success = False

        self._last_send = None
        self._cache_name = f'{phone}otp'
        self._code = None
        self._send = 0
        self._temporary_blocked = False
        self._blocked_time = None
        self._failed_retries_count = 0

        self._get_cache()

    @property
    def debug_dict(self):
        return self.__dict__ if self.test else None

    @property
    def retries_left(self):
        return settings.OTP["MAX_FAILED_RETRIES"] - self._failed_retries_count

    def _get_cache(self):
        data = cache.get(self._cache_name)
        if data:
            self.cache_exists = True
            for key, value in data.items():
                if key not in ['phone', 'cache_name', 'cache_exists']:
                    setattr(self, key, value)
        else:
            self.cache_exists = False

    def _set_resend_time(self):
        if timezone.now() - self._last_send < timedelta(seconds=settings.OTP['RESEND_TTL']):
            delta = timedelta(seconds=settings.OTP['RESEND_TTL']) - (timezone.now() - self._last_send)
            delta = delta.seconds
        else:
            delta = 0
        self.resend_time = delta

    def _set_code(self):
        self._code = get_random_string(length=4, allowed_chars='0123456789')

    def _raise_temporary_blocked(self):
        time_left = (settings.OTP['FAILED_RETRIES_TTL'] - (timezone.now() - self._blocked_time).seconds) // 60
        raise TemporaryBlocked(f'Temporary blocked time left: {time_left} minutes', time_left)

    def _check_temporary_blocked(self):
        if self._temporary_blocked and \
                (timezone.now() - self._blocked_time) < timedelta(seconds=settings.OTP['FAILED_RETRIES_TTL']):
            self._raise_temporary_blocked()

    def _set_temporary_blocked(self):
        self._failed_retries_count += 1
        if self._failed_retries_count == settings.OTP['MAX_FAILED_RETRIES']:
            self._temporary_blocked = True
            self._blocked_time = timezone.now()
            cache.set(self._cache_name, self.__dict__, settings.OTP['TTL'])
            self._raise_temporary_blocked()

    def _check_resend(self):
        if self._last_send and (timezone.now() - self._last_send < timedelta(seconds=settings.OTP['RESEND_TTL'])):
            time_left = settings.OTP['RESEND_TTL'] - (timezone.now() - self._last_send).seconds
            raise ResendNotAvailable(f'Resend not available wait for {time_left} seconds', time_left)

    def _delete_cache(self):
        cache.delete(self._cache_name)

    def send_sms(self):
        self._check_temporary_blocked()
        self._check_resend()
        self._set_code()
        self._last_send = timezone.now()
        self._send += 1
        cache.set(self._cache_name, self.__dict__, settings.OTP['TTL'])
        if not self.test:
            send_sms.delay(self.phone, self._code)
        self._set_resend_time()

    def check_code(self, code):
        self._check_temporary_blocked()
        cache.set(self._cache_name, self.__dict__, settings.OTP['TTL'])
        if self._code == code or (self.test and code == '9876'):
            self._delete_cache()
            self.check_success = True
            return
        self._set_temporary_blocked()
        cache.set(self._cache_name, self.__dict__, settings.OTP['TTL'])
        raise InvalidCodeException(
            f'Retries left: {self.retries_left}', settings.OTP["MAX_FAILED_RETRIES"] - self._failed_retries_count
        )
