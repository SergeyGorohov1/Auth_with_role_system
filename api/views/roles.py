from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.permissions import CanAccessObject
from api.serializers.roles import AccessRolesRulesSerializer, RoleSerializer
from users.models import AccessRolesRules, Role


class AccessRolesRulesViewSet(ModelViewSet):
    """Viewset прав доступа"""
    queryset = AccessRolesRules.objects.all()
    serializer_class = AccessRolesRulesSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='permissions')]


class RoleViewSet(ModelViewSet):
    """Viewset ролей"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='roles')]
