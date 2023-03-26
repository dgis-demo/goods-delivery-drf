from rest_framework import mixins, permissions, viewsets
from ua_parser import user_agent_parser

from apps.notifications.models import DeviceToken
from apps.notifications.serializers import DeviceTokenSerializer


class DeviceTokenViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'list': DeviceTokenSerializer,
        'create': DeviceTokenSerializer,
        'update': DeviceTokenSerializer,
        'destroy': DeviceTokenSerializer,
    }
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DeviceToken.objects.none()

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    def perform_create(self, serializer):
        user_agent = self.request._request.META.get('HTTP_USER_AGENT')
        device = self._get_device(user_agent)
        serializer.save(device=device, user=self.user)

    def perform_update(self, serializer):
        serializer.save(user=self.user)

    def get_queryset(self):
        return DeviceToken.objects.filter(user=self.user)

    @property
    def user(self):
        return self.request.user

    @staticmethod
    def _get_device(user_agent: str) -> str:
        device = ''
        try:
            device = user_agent_parser.ParseDevice(user_agent)
        finally:
            return device
