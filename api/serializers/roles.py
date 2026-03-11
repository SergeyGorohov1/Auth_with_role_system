from rest_framework import serializers

from users.models import AccessRolesRules, Role


class AccessRolesRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRolesRules
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
