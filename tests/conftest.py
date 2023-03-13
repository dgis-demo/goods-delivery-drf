import uuid

import pytest
from pytest_factoryboy import LazyFixture, register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.factories import UserFactory

# AUTHENTICATION
register(UserFactory)
register(
    UserFactory,
    "customer_user",
    role="customer"
)
register(
    UserFactory,
    "courier_user",
    role="courier"
)
register(UserFactory, "first_user")
register(UserFactory, "second_user")

register(UserFactory, "customer")


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def api_customer_client(customer_user):
    client = APIClient()
    refresh = RefreshToken.for_user(customer_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def api_courier_client(courier_user):
    client = APIClient()
    refresh = RefreshToken.for_user(courier_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user
