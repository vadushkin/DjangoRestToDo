from rest_framework import permissions


class IsOwnerOrAdminPermission(permissions.BasePermission):
    """
    Check is object owner or is staff.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
