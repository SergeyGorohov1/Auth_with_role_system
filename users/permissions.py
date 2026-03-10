from elements.models import Element
from users.models import AccessRolesRules, User


def can_access_object(request, object):
    """
        Право, реализующее основную логику работы с правами для данного проекта.
        Доступ к контроллеру устанавливается в зависимости от прав, описанных в
        объектах модели AccessRolesRules.
    """
    role = request.user.role

    try:
        element = Element.objects.get(name=object)
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


def is_owner(request, obj):
    """Право, для проверки владельца обекта"""
    if type(obj) is User:
        return obj == request.user
    else:
        return obj.owner == request.user
