import pytest

from apps.accounts.models import User
from apps.accounts.roles import Permissions, UserRole


@pytest.mark.django_db
def test_create_user(user):
    assert isinstance(user, User)


@pytest.mark.django_db
@pytest.mark.parametrize('user__role', ['customer'])
def test_user_role(user, user__role):
    assert user.role == UserRole.CUSTOMER


@pytest.fixture
def set_user_role(user):
    Permissions.CRUD_PERMISSIONS = {
        user.role: ['view']
    }
    Permissions.MODULE_PERMISSIONS = {
        user.role: {
            'goods': ['category']
        }
    }
    return user
