from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


handler500 = 'apps.utils.exceptions.common_server.server_error'
handler404 = 'apps.utils.exceptions.common_server.not_found_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('apps.accounts.api')),
        path('notifications/', include('apps.notifications.api')),
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger/',
             SpectacularSwaggerView.as_view(url_name='schema'),
             name='swagger'),
        path('redoc/',
             SpectacularRedocView.as_view(url_name='schema'),
             name='redoc'),
    ]),),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
