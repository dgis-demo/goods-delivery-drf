from rest_framework import permissions

from apps.accounts.models import User, UserRole


class IsActiveStoreWorker(permissions.BasePermission):
    """
    Allows an access only for active store workers
    """

    message = 'User must be a store worker'

    def has_permission(self, request, view):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()

        if not user:
            self.message = 'Store worker is not found'
            return False

        if not user.is_active:
            self.message = 'Store worker is not active'
            return False

        return user.role == UserRole.STORE_WORKER
