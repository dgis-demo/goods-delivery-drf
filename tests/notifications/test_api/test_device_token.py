from http import HTTPStatus

import pytest
from django.shortcuts import reverse


class TestDeviceToken:
    url = reverse('notifications:create-device-token')

    @pytest.mark.django_db
    def test_list_success(self, api_client, device_token):
        response = api_client.get(self.url)

        assert response.status_code == HTTPStatus.OK
        assert response.json()[0]['id'] == device_token.id
