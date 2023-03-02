import uuid

import pytest
from pytest_factoryboy import LazyFixture, register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.factories import UserFactory
from apps.measurement.factories import CityFactory, CountryFactory, CurrencyFactory

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

# MEASUREMENT
register(CountryFactory, "country", short_name='CO', alpha2='CO', alpha3='CO3', code='CO3')
register(CountryFactory, "first_country", short_name='FR', alpha2='FR', alpha3='FR3', code='FR3')
register(CountryFactory, "second_country", short_name='SC', alpha2='SC', alpha3='SC3', code='SC3')

register(CityFactory)

register(CurrencyFactory)
register(CurrencyFactory, "first_currency", country=LazyFixture("first_country"))
register(CurrencyFactory, "second_currency", country=LazyFixture("second_country"))


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
def zone_filters():
    return [{
        'x1': 49.18624815861086,
        'y1': 1.734295621436286,
        'x2': 48.57387156249436,
        'y2': 2.850472216686399
    }]


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
