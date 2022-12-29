from rest_framework import permissions
from .models import User
from rest_framework.views import View

class IsReviewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS: return True

        if (
            request.user and 
            request.user.is_authenticated and 
            request.user.is_superuser
        ): 
            return True

        if (
            request.user and 
            request.user.is_authenticated and 
            request.user.is_critic
        ): 
            return True
        
        return False
