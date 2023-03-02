from rest_framework.exceptions import PermissionDenied


class InvalidCodeException(AssertionError):
    pass


class TemporaryBlocked(PermissionDenied):
    pass


class ResendNotAvailable(PermissionDenied):
    pass
