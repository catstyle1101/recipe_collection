from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """
    ReadOnly permission.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsAdmin(permissions.BasePermission):
    """
    Admin permission.
    """
    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and (user.is_admin or user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser))


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Author or read only permission.
    """
    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and user.is_user
            or request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )