from django.urls import path

from apps.notifications.views import DeviceTokenViewSet


app_name = 'notifications'

urlpatterns = [
    path('devicetoken/', DeviceTokenViewSet.as_view({'get': 'list', 'post': 'create'}), name='create-device-token'),
    path('devicetoken/<pk>/', DeviceTokenViewSet.as_view({'patch': 'update', 'delete': 'destroy'}),
         name='details-device-token'),
]
