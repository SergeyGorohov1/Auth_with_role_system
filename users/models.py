from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Role(models.Model):
    ROLES = [
        ("admin", "Админ"),
        ("manager", "Менеджер"),
        ("user", "Пользователь"),
        ("guest", "Гость")
    ]

    name = models.CharField(max_length=7, choices=ROLES, default="user", unique=True, verbose_name="роль")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="имя")
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="фамилия")
    patronymic = models.CharField(max_length=150, null=True, blank=True, verbose_name="отчество")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

# class AccessRolesRules(models.Model):
