from django.urls import path

from .views import CityViewSet, CountryViewSet


app_name = 'measurement'

urlpatterns = [
    path(
        'cities/<int:pk>/',
        CityViewSet.as_view({'get': 'retrieve'}),
        name='cities-detail',
    ),
    path(
        'countries/',
        CountryViewSet.as_view({'get': 'list'}),
        name='countries-list',
    ),
]
