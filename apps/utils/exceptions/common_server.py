from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if hasattr(response.data, 'detail'):
            response.data = {
                'detail': {'message': [response.data['detail']]},
                'status_code': response.status_code
            }
        else:
            response.data = {
                'detail': {'message': [response.data]},
                'status_code': response.status_code
            }

    return response


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'status_code': 500,
        'detail': {'message': [_('Something went wrong')]}
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def not_found_error(request, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {
        'status_code': 404,
        'detail': {'message': [_('Page not found')]}
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
