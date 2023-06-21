from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ReadOnlyIfAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS) and bool(request.user and request.user.is_authenticated)
