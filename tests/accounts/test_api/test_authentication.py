import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_create_courier_success(api_client, fake):
    url = reverse('auth:courier-login-phone')
    response = api_client.post(
        url,
        data={
            'phone': f'+{fake.msisdn()}',
        },
    )

    assert response.status_code == 200
