from django.core.management import call_command
from django.core.management.base import BaseCommand
from users.models import User, Role, AccessRolesRules
from elements.models import Element


class Command(BaseCommand):
    def handle(self, *args, **options):
        roles = ["admin", "user", "manager", "guest"]
        elements = ["users", "products", "orders", "roles", "permissions", "elements"]

        for role_name in roles:
            role, created = Role.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Роль {role_name} успешно создана")
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(f"Роль {role_name} уже существует")
                )

        for element_name in elements:
            element, created = Element.objects.get_or_create(name=element_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Элемент {element_name} успешно создан")
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(f"Элемент {element_name} уже существует")
                )

        for i, role_name in enumerate(roles):
            role = Role.objects.get(name=role_name)
            user, created = User.objects.get_or_create(email=f"{role_name}@mail.ru", role=role)

            password = "Password+123"
            user.set_password(password)
            if role_name == "admin":
                user.is_staff = True
                user.is_superuser = True
            user.save()

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Пользователь успешно создан. email: {user.email}; password: {password}")
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(f"Пользователь уже существует. email: {user.email}; password: {password}")
                )

        call_command('loaddata', "fixtures/access_roles_rules.json")