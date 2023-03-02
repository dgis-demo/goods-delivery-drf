from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .tasks import send_push_notifications

from .managers import UserAdminProxyManager, UserBaseProxyManager
from .otp import OTP
from .roles import RolePermission, UserRole
from .validatiors import phone_validator


class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=True, null=True)
    phone = models.CharField(validators=[phone_validator], max_length=21, blank=True, null=True, unique=True)
    is_phone_verified = models.BooleanField(_('is phone verified'), default=False)
    role = models.CharField(_('user role'), max_length=20, choices=UserRole.USER_ROLE_CHOICES, null=True)
    country = models.CharField(
        verbose_name=_('country'),
        max_length=3,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    @property
    def _otp(self):
        return OTP(self.phone)

    @property
    def status(self):
        if hasattr(self, 'user_stores'):
            return self.user_stores.is_verified

    def send_otp(self):
        otp = self._otp
        otp.send_sms()
        return otp

    def check_otp(self, otp_code):
        otp = self._otp
        otp.check_code(otp_code)
        return otp

    def send_push_notification(self, title, body):
        tokens = list(self.device_tokens.filter(is_enabled=True).values_list('token', flat=True))
        if tokens:
            send_push_notifications.delay(tokens, title, body)

    def has_perm(self, perm, obj=None):
        if RolePermission(self).user_has_permission(perm):
            return True
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        if RolePermission(self).user_has_module_permissions(app_label):
            return True
        return super(User, self).has_module_perms(app_label)

    @property
    def tokens(self):
        return list(self.device_tokens.values_list('token', flat=True))

    @property
    def store(self):
        if hasattr(self, 'userstore'):
            return self.userstore.store

    def save(self, *args, **kwargs):
        roles = (
            self.role == UserRole.STORE_WORKER,
            self.role == UserRole.BACKOFFICE_COUNTRY_EMPLOYEE,
        )
        if any(roles) and self.store and not self.country:
            self.country = self.store.city.country
        super().save(*args, **kwargs)


class UserCustomerProxy(User):
    objects = UserBaseProxyManager()

    default_role = UserRole.CUSTOMER
    default_is_staff = False
    default_is_superuser = False

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        proxy = True


class UserCourierProxy(User):
    objects = UserBaseProxyManager()

    default_role = UserRole.COURIER
    default_is_staff = False
    default_is_superuser = False

    class Meta:
        verbose_name = _('courier')
        verbose_name_plural = _('couriers')
        proxy = True


class UserStoreProxy(User):
    objects = UserBaseProxyManager()

    default_role = UserRole.STORE_WORKER
    default_is_staff = True
    default_is_superuser = False

    class Meta:
        verbose_name = _('store worker')
        verbose_name_plural = _('store workers')
        proxy = True


class UserBOCountryProxy(User):
    objects = UserBaseProxyManager()

    default_role = UserRole.BACKOFFICE_COUNTRY_EMPLOYEE
    default_is_staff = True
    default_is_superuser = False

    class Meta:
        verbose_name = _('backoffice country employee')
        verbose_name_plural = _('backoffice country workers')
        proxy = True


class UserBOCompanyProxy(User):
    objects = UserBaseProxyManager()

    default_role = UserRole.BACKOFFICE_COMPANY_EMPLOYEE
    default_is_staff = True
    default_is_superuser = False

    class Meta:
        verbose_name = _('backoffice company employee')
        verbose_name_plural = _('backoffice company workers')
        proxy = True


class UserAdminProxy(User):
    objects = UserAdminProxyManager()

    default_role = UserRole.ADMINISTRATOR
    default_is_staff = True
    default_is_superuser = True

    class Meta:
        verbose_name = _('administrator')
        verbose_name_plural = _('administrators')
        proxy = True


class UserSupportProxy(User):
    objects = UserBaseProxyManager()

    default_role = UserRole.SUPPORT
    default_is_staff = True
    default_is_superuser = False

    class Meta:
        verbose_name = _('support')
        verbose_name_plural = _('supports')
        proxy = True
