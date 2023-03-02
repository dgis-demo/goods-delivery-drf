from rest_framework import decorators, generics, permissions, response, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase

from apps.utils.permissions.common import IsActiveStoreWorker

from .serializers import (
    UserCodeVerifySerializer,
    UserLoginPhoneSerializer,
)


class LoginPhoneView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = UserLoginPhoneSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request,
                **kwargs,
            },
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginUsernameView(TokenObtainPairView):
    """Extension of TokenObtainPairView with user id and registration stage."""
    permission_classes = (AllowAny,)


class LoginStoreWorkerView(TokenObtainPairView):
    permission_classes = (IsActiveStoreWorker, )


class TokenObtainView(TokenViewBase):
    serializer_class = UserCodeVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
