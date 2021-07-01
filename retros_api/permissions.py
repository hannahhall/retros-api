from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """Only allow the student or an instructor to interact with object

        Returns:
            Boolean: Whether the user owns the object or is an admin
        """
        if request.method in ['OPTIONS', 'POST']:
            return True

        try:
            owner = obj.user
        except AttributeError:
            owner = obj.student.user
        return owner == request.user or request.user.is_staff
