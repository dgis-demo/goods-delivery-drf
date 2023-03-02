from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .roles import UserRole


app_name = 'auth'

urlpatterns = [
    path(
        'login/phone/customer/',
        views.LoginPhoneView.as_view(),
        {'role': UserRole.CUSTOMER},
        name='customer-login-phone',
    ),
    path(
        'login/phone/courier/',
        views.LoginPhoneView.as_view(),
        {'role': UserRole.COURIER},
        name='courier-login-phone',
    ),
    path(
        'login/phone/verify/',
        views.TokenObtainView.as_view(),
        name='login-verify',
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh',
    ),

    path(
        'login/username/',
        views.LoginUsernameView.as_view(),
        name='login-username',
    ),

    path(
        'login/username/store_worker/',
        views.LoginStoreWorkerView.as_view(),
        name='store-worker-login-username',
    ),
]
