from django.conf import settings
from twilio.rest import Client as TwilioClient


class AbstractSmsSender:
    def set_up(self, *args, **kwargs):
        raise NotImplementedError

    def send(self, text: str, to: str, *args, **kwargs):
        raise NotImplementedError


class TwilioTestSmsSender(AbstractSmsSender):
    SETTINGS_NAME = 'TwilioTest'

    def __init__(self):
        self.client = None
        self.messaging_service_sid = None

    def set_up(self, *args, **kwargs):
        sender = settings.SMS_SENDER[self.SETTINGS_NAME]
        self.client = TwilioClient(
            sender['account_sid'],
            sender['auth_token'],
        )
        self.messaging_service_sid = settings['messaging_service_sid']

    def send(self, text, to, *args, **kwargs):
        return self.client.messages.create(
            messaging_service_sid=self.messaging_service_sid,
            body=text,
            to=to
        )


class Stub(AbstractSmsSender):
    def set_up(self, *args, **kwargs):
        return

    def send(self, *args, **kwargs):
        return


senders = {
    'TwilioTest': TwilioTestSmsSender,
    'Stub': Stub,
}
