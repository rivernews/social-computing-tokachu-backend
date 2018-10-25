from rest_framework.permissions import  BasePermission

class AllowOptionsIsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return request.user and request.user.is_superuser
