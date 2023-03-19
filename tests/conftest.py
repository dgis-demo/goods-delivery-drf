import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.accounts.factories import UserFactory
from tests.notifications.factories import DeviceTokenFactory


# AUTHENTICATION
register(UserFactory, 'user')

# NOTIFICATIONS
register(DeviceTokenFactory, 'device_token')


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client
