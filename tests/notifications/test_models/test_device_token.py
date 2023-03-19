import pytest

from apps.notifications.models import DeviceToken


@pytest.mark.django_db
def test_create_device_token(device_token):
    assert isinstance(device_token, DeviceToken)
