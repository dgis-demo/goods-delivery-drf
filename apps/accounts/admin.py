from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import (
    UserAdminProxy,
    UserBOCompanyProxy,
    UserBOCountryProxy,
    UserCourierProxy,
    UserCustomerProxy,
    UserStoreProxy,
    UserSupportProxy,
)

from .roles import UserRole


class BaseUserCreationProxyForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.Meta.model.default_role
        user.is_staff = self.Meta.model.default_is_staff
        user.is_superuser = self.Meta.model.default_is_superuser
        if commit:
            user.save()
        return user


class BaseAdminProxyMixin:
    fieldsets = (
        (None, {'fields': ('username', ('phone', 'is_phone_verified'), 'password', 'country')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'role'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined', 'is_phone_verified')

    add_form = BaseUserCreationProxyForm


@admin.register(UserCustomerProxy)
class UserCustomerProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    pass


@admin.register(UserCourierProxy)
class UserCourierProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    additional_readonly_fields = ['role', 'is_active', 'is_superuser', 'is_staff']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.role == UserRole.BACKOFFICE_COUNTRY_EMPLOYEE:
            queryset = queryset.filter(country=request.user.country)

        if request.user.role == UserRole.STORE_WORKER:
            queryset = queryset.filter(user_stores__store=request.user.user_stores.store)

        return queryset

    def get_object(self, request, object_id, from_field=None):
        self.readonly_fields = BaseAdminProxyMixin.readonly_fields

        if request.user.role != UserRole.ADMINISTRATOR:
            self.readonly_fields = tuple(list(self.readonly_fields) + self.additional_readonly_fields)

        return super(UserCourierProxyAdmin, self).get_object(request, object_id, from_field)


@admin.register(UserStoreProxy)
class UserStoreProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    store_worker_readonly_fields = (
        'is_superuser',
        'is_staff',
        'username',
        'country',
        'role',
    )

    def get_queryset(self, request):
        user = request.user
        queryset = super().get_queryset(request)

        if user.role == UserRole.BACKOFFICE_COUNTRY_EMPLOYEE:
            queryset = queryset.filter(country=user.country)

        if user.role == UserRole.STORE_WORKER:
            queryset = queryset.filter(user_stores__store=user.user_stores.store)

        return queryset

    def get_readonly_fields(self, request, obj=None) -> tuple:
        readonly_fields = super().get_readonly_fields(request, obj) or []
        user = request.user

        if user.role == UserRole.BACKOFFICE_COUNTRY_EMPLOYEE or user.role == UserRole.STORE_WORKER:
            readonly_fields += self.store_worker_readonly_fields

        return readonly_fields


@admin.register(UserBOCountryProxy)
class UserBOCountryProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    pass


@admin.register(UserBOCompanyProxy)
class UserBOCompanyProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    pass


@admin.register(UserAdminProxy)
class UserAdminProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    pass


@admin.register(UserSupportProxy)
class UserSupportProxyAdmin(BaseAdminProxyMixin, UserAdmin):
    pass
