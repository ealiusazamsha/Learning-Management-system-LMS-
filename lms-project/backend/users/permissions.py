from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """Allow non-destructive actions for all, admin for others."""

    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user and request.user.is_staff
