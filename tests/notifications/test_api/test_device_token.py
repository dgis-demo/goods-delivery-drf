from http import HTTPStatus

import pytest
from django.shortcuts import reverse

from apps.notifications.models import DeviceToken


class TestDeviceToken:
    url = reverse('notifications:create-device-token')

    @pytest.mark.django_db
    def test_list_success(self, api_client, device_token):
        response = api_client.get(self.url)

        assert response.status_code == HTTPStatus.OK
        assert response.json()[0]['id'] == device_token.id

    @pytest.mark.django_db
    # update, destroy
    def test_create_success(self, api_client, fake):
        response = api_client.post(
            self.url,
            data={
                'device_id': fake.word(),
                'device_type': 'IOS',
                'token': fake.word(),
            },
        )

        assert response.status_code == HTTPStatus.CREATED
        assert DeviceToken.objects.last().id == response.json()['id']
