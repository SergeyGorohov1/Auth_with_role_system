from django.contrib import admin

from users.models import User, Role, AccessRolesRules

admin.site.register(User)
admin.site.register(Role)


@admin.register(AccessRolesRules)
class AccessRolesRulesAdmin(admin.ModelAdmin):
    list_display = ["role", "element", "read_all_permission", "create_permission", "update_all_permission",
                    "delete_all_permission"]
    list_filter = ["role", "element"]
