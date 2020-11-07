from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnPermission(BasePermission):
    """Check if this your on thing."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Return if this object has permission."""
        if not request.user:
            return False

        if request.method in SAFE_METHODS:
            return True

        return bool(obj.user.id == request.user.id)


class ManageSessionPermission(BasePermission):
    """Check if this session for you or not."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Return if this object has permission."""
        if not request.user:
            return False

        return bool(obj.owner.id == request.user.id)


class ManageRolePermission(BasePermission):
    """Check if this session for you or not."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Return if this object has permission."""
        if not request.user:
            return False

        return bool(obj.chat_session.owner.id == request.user.id)
