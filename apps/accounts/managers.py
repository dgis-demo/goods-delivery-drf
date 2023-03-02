from django.contrib.auth.models import UserManager
from django.db import models

from .roles import UserRole


class UserBaseProxyManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(role=self.model.default_role)

    def _create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('role', self.model.default_role)
        extra_fields['is_staff'] = self.model.default_is_staff
        extra_fields['is_superuser'] = self.model.default_is_superuser
        return super(UserBaseProxyManager, self)._create_user(username, email, password, **extra_fields)


class UserAdminProxyManager(UserManager):
    role = UserRole.ADMINISTRATOR

    def get_queryset(self):
        return super().get_queryset().filter(
            models.Q(role=self.role) | models.Q(is_superuser=True)
        )
