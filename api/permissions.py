from rest_framework.permissions import BasePermission
from users.models import AccessRolesRules


class CanAccessObject(BasePermission):
    def __init__(self, object):
        self.object = object

    def has_permission(self, request, view):
        user = request.user
        role = user.role
        if role:
            try:
                access_roles_rules = AccessRolesRules.objects.get(role=role, element=self.object)
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
