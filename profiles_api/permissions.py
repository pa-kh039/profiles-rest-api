from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''

    def has_object_permission(self,request,view,obj):
        '''Check user is trying to edit their own profile only'''
        if request.method in permissions.SAFE_METHODS:
            # reading all user profiles, creating a new profile,etc. dont need extra permission checks, these are safe methods
            return True
        
        return obj.id==request.user.id
    
