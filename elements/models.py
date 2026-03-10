from django.db import models


class Element(models.Model):
    """Бизнес эл-ты, присутствующие в проекте"""
    ELEMENTS_IN_PROJECT = [
        ("users", "Пользователи"),
        ("products", "Товары"),
        ("orders", "Заказы"),
        ("roles", "Роли"),
        ("permissions", "Права доступа"),
        ("elements", "Элементы"),
    ]

    name = models.CharField(max_length=11, choices=ELEMENTS_IN_PROJECT, unique=True, verbose_name="Элемент")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
