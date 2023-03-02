class UserRole:
    CUSTOMER = 'customer'
    COURIER = 'courier'
    STORE_WORKER = 'store'
    BACKOFFICE_COUNTRY_EMPLOYEE = 'bo_country'
    BACKOFFICE_COMPANY_EMPLOYEE = 'bo_company'
    ADMINISTRATOR = 'admin'
    SUPPORT = 'support'

    USER_ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (COURIER, 'Courier'),
        (STORE_WORKER, 'Store worker'),
        (BACKOFFICE_COUNTRY_EMPLOYEE, 'Backoffice country employee'),
        (BACKOFFICE_COMPANY_EMPLOYEE, 'Backoffice company employee'),
        (ADMINISTRATOR, 'Administrator'),
        (SUPPORT, 'Support'),
    ]


class Permissions:
    """
    MODULE_PERMISSIONS must be a dict of dicts containing crud permissions like below:
    { 'app_name': {'app_model': ['crud_permission1', 'crud_permission2']}

    Example:
    MODULE_PERMISSIONS = {
        UserRole.CUSTOMER: {
            'goods': {'good': ['view', 'add']},
            'orders': {'order': ['delete']}
        },
        UserRole.STORE_WORKER: {
            'goods': {'good': ['view', 'add', 'change', 'delete']},
        }
    }
    """
    MODULE_PERMISSIONS = {
        UserRole.STORE_WORKER: {
            'accounts': {
                'usercourierproxy': ['view', 'add', 'change', 'delete'],
                'userstoreproxy': ['view', 'add', 'change', 'delete'],
            },
            'goods': {
                'goodstore': ['view', 'change'],
                'good': ['view'],
                'leftoverlog': ['view', 'add'],
            },
            'orders': {
                'order': ['view', 'change'],
                'ordergood': ['view'],
                'ordergoodback': ['view', 'add', 'change', 'delete'],
            },
        },
        UserRole.BACKOFFICE_COUNTRY_EMPLOYEE: {
            'accounts': {
                'usercourierproxy': ['view', 'add', 'change', 'delete'],
                'userstoreproxy': ['view', 'add', 'change', 'delete'],
            },
            'goods': {
                'good': ['view', 'add', 'change', 'delete'],
            },
            'notifications': {
                'pushtemplate': ['view', 'add', 'change', 'delete'],
            }
        },
        UserRole.BACKOFFICE_COMPANY_EMPLOYEE: {
            'goods': {
                'good': ['view', 'add', 'change', 'delete'],
            },
            'notifications': {
                'pushtemplate': ['view', 'add', 'change', 'delete'],
            },
        },
    }


class RolePermission:
    def __init__(self, user):
        self.user = user
        self.module_permissions = Permissions.MODULE_PERMISSIONS

    @property
    def user_permissions(self) -> list:
        try:
            permissions = []
            for app_name, model_list in self.module_permissions[self.user.role].items():
                for model_name, crud_permissions in model_list.items():
                    for crud in crud_permissions:
                        permission_name = f'{app_name}.{crud}_{model_name}'
                        permissions.append(permission_name)
            return permissions
        except (KeyError, TypeError, AttributeError):
            return []

    @property
    def available_apps(self) -> list:
        try:
            return list(self.module_permissions[self.user.role].keys())
        except (KeyError, TypeError, AttributeError):
            return []

    def user_has_permission(self, permission_name: str) -> bool:
        return bool(self.user_has_role() and permission_name in self.user_permissions)

    def user_has_module_permissions(self, app_name: str) -> bool:
        return bool(self.user_has_role() and app_name in self.available_apps)

    def user_has_role(self) -> bool:
        if not hasattr(self.user, 'role'):
            return False

        if not self.user.role:
            return False

        return True
