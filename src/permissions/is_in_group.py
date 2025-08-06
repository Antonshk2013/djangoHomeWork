from rest_framework.permissions import BasePermission

class IsInGroup(BasePermission):
    def has_permission(self, request, view):
        ...