from rest_framework.permissions import BasePermission

from elements.models import Element
from users.models import AccessRolesRules, User


class CanAccessObject(BasePermission):
    def __init__(self, object):
        self.object = object

    def has_permission(self, request, view):
        role = request.user.role

        try:
            element = Element.objects.get(name=self.object)
        except Element.DoesNotExist:
            return False

        if role:
            try:
                access_roles_rules = AccessRolesRules.objects.get(role=role, element=element)
                if request.method == "POST":
                    return access_roles_rules.create_permission
                elif request.method == "GET":
                    return access_roles_rules.read_all_permission
                elif request.method in ["PUT", "PATCH"]:
                    return access_roles_rules.update_all_permission
                elif request.method == "DELETE":
                    return access_roles_rules.delete_all_permission
            except AccessRolesRules.DoesNotExist:
                return False
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if type(obj) == User:
            return obj == request.user
        else:
            return obj.owner == request.user
