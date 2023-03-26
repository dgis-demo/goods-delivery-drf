from http import HTTPStatus

import pytest
from django.shortcuts import reverse

from apps.notifications.models import DeviceToken


class TestDeviceToken:
    url = reverse('notifications:create-device-token')
    details_url = 'notifications:details-device-token'

    @pytest.mark.django_db
    def test_list_success(self, api_client, device_token):
        response = api_client.get(self.url)

        assert response.status_code == HTTPStatus.OK
        assert response.json()[0]['id'] == device_token.id

    @pytest.mark.django_db
    def test_create_success(self, api_client, fake):
        response = api_client.post(
            self.url,
            data={
                'device_id': fake.word(),
                'device_type': DeviceToken.DeviceType.IOS,
                'token': fake.word(),
            },
        )

        assert response.status_code == HTTPStatus.CREATED
        assert DeviceToken.objects.last().id == response.json()['id']

    @pytest.mark.django_db
    def test_update_success(self, api_client, device_token, fake):
        response = api_client.patch(
            reverse(self.details_url, kwargs={'pk': device_token.id}),
            data={
                'device_id': fake.word(),
                'device_type': DeviceToken.DeviceType.ANDROID,
                'token': fake.word(),
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert response.json()['id'] == device_token.id
        assert response.json()['device_type'] == DeviceToken.DeviceType.ANDROID

    @pytest.mark.django_db
    def test_destroy_success(self, api_client, device_token):
        response = api_client.delete(
            reverse(self.details_url, kwargs={'pk': device_token.id}),
        )

        assert response.status_code == HTTPStatus.NO_CONTENT
        assert DeviceToken.objects.count() == 0
