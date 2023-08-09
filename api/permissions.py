from django.conf import settings
from rest_framework.permissions import BasePermission

# from django.conf import settings
SAFE_METHODS = ('GET',)


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return False

        return bool(request.user and request.user.is_staff)
