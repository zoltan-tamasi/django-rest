from rest_framework import permissions
from .models import Authority

class IsOwnerOrHasAuthority(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        authority_exists = Authority.objects.filter(user=request.user).filter(blogpost=obj).count() > 0

        return obj.owner == request.user or authority_exists