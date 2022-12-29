from rest_framework import permissions
from rest_framework.views import View

class IsAccountPermission(permissions.BasePermission):
    
    def has_permission(self, request, view: View) -> bool:
        
        if request.method == "POST": return True
            
        if (
            request.method in permissions.SAFE_METHODS and
            request.user.is_authenticated and
            request.user.is_superuser
        ):
            return True

        return False


class IsMoviePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS: return True

        if (
            request.user and 
            request.user.is_authenticated and 
            request.user.is_superuser
        ): 
            return True
        
        return False

