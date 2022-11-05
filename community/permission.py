from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import Channels

class IsCommunityAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == obj.community.community_admin
    
