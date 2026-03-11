from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    password_confirm = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "patronymic", "password", "password_confirm"]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"error": "Пароли не совпадают"})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User(**validated_data)
        try:
            # Доп. валидация на схожесть пароля с email
            validate_password(validated_data["password"], user)
            user.set_password(user.password)
            user.save()
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "patronymic"]


class ChangePasswordSerializer(serializers.Serializer):
    """Сериализатор для смены пароля пользователя"""
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Старый пароль указан не правильно.")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"error": "Пароли не совпадают"})

        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError({"error": "Новый пароль должен отличаться от старого."})

        validate_password(data['new_password'], self.context['request'].user)

        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
