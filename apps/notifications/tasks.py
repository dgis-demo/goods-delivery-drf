from django.conf import settings
from firebase_admin import credentials, initialize_app, messaging

from Project.celery import app


FIREBASE_APP = settings.FIREBASE_CREDENTIALS and initialize_app(
    credentials.Certificate(settings.FIREBASE_CREDENTIALS)
)


@app.task
def send_push_notifications(tokens: list, title: str, body: str, firebase_app=FIREBASE_APP):
    """
    You can find these methods into the following SDK:
    https://firebase.google.com/docs/reference/admin/python/
    """
    if firebase_app:
        notification = messaging.Notification(title=title, body=body)
        multicast_message = messaging.MulticastMessage(tokens, notification=notification)

        messaging.send_multicast(multicast_message, app=firebase_app)
