from http import HTTPStatus

import pytest
from django.contrib.auth.hashers import make_password
from django.shortcuts import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import User
from apps.accounts.roles import UserRole


class TestCourierLogin:
    url = reverse('auth:courier-login-phone')
    role = UserRole.COURIER

    @pytest.mark.django_db
    def test_login_success(self, api_client, fake):
        phone = f'+{fake.msisdn()}'
        response = api_client.post(
            self.url,
            data={
                'phone': phone,
            },
        )
        user = User.objects.get(phone=phone)

        assert response.status_code == HTTPStatus.OK
        assert user.role == self.role

    @pytest.mark.django_db
    def test_login_bad_request(self, api_client, fake):
        phone = f'+{fake.unique.word()}'
        response = api_client.post(
            self.url,
            data={
                'phone': phone,
            },
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST


class TestCustomerLogin(TestCourierLogin):
    url = reverse('auth:customer-login-phone')
    role = UserRole.CUSTOMER


class TestLoginUsername:
    url = reverse('auth:login-username')

    @pytest.mark.django_db
    def test_login_user_success(self, api_client, user, fake):
        password = fake.unique.word()
        user.password = make_password(password)
        user.save()

        response = api_client.post(
            self.url,
            data={
                'username': user.username,
                'password': password,
            },
        )

        assert response.status_code == HTTPStatus.OK

    @pytest.mark.django_db
    def test_login_unauthorised(self, api_client, user):
        response = api_client.post(
            self.url,
            data={
                'username': user.username,
                'password': user.password,
            },
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED


class TestLoginStoreWorker(TestLoginUsername):
    url = reverse('auth:store-worker-login-username')

    @pytest.mark.django_db
    def test_login_user_success(self, api_client, user, fake):
        user.role = UserRole.STORE_WORKER
        user.save()
        super().test_login_user_success(api_client, user, fake)

    @pytest.mark.django_db
    def test_login_unauthorised(self, api_client, user):
        pass

    @pytest.mark.django_db
    def test_login_forbidden(self, api_client, user):
        response = api_client.post(
            self.url,
            data={
                'username': user.username,
                'password': user.password,
            },
        )

        assert response.status_code == HTTPStatus.FORBIDDEN


class TestTokenRefresh:
    url = reverse('auth:token-refresh')

    @pytest.mark.django_db
    def test_refresh_token_success(self, api_client, user):
        refresh = RefreshToken.for_user(user)
        response = api_client.post(
            self.url,
            data={
                'refresh': str(refresh),
            },
        )

        assert response.status_code == HTTPStatus.OK

    @pytest.mark.django_db
    def test_refresh_token_unauthorised(self, api_client, user):
        response = api_client.post(
            self.url,
            data={
                'refresh': user.username,
            },
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED
