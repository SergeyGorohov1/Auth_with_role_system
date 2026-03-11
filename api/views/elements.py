from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.permissions import CanAccessObject
from api.serializers.elements import ElementSerializer
from elements.models import Element


class ElementViewSet(ModelViewSet):
    """Viewset элементов"""
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='elements')]


class ProductsView(APIView):
    """Mock-view для Продуктов"""
    def get(self, request, pk=None):
        if pk:
            return Response("Продукт")
        return Response(["Продукт_1", "Продукт_2", "Продукт_3"])

    def post(self, request):
        return Response(
            {"message": "Продукт добавлен"},
            status=status.HTTP_201_CREATED
        )

    def put(self, request, pk=None):
        return Response({
            "message": "Продукт изменен",
        })

    def patch(self, request, pk=None):
        return Response({
            "message": "Продукт изменен",
        })

    def delete(self, request, pk=None):
        return Response(
            {"message": "Продукт удален"},
            status=status.HTTP_204_NO_CONTENT
        )

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='products')]


class OrdersView(APIView):
    """Mock-view для Заказов"""

    def get(self, request, pk=None):
        if pk:
            return Response("Заказ")
        return Response(["Заказ_1", "Заказ_2", "Заказ_3"])

    def post(self, request):
        return Response(
            {"message": "Заказ добавлен"},
            status=status.HTTP_201_CREATED
        )

    def put(self, request, pk=None):
        return Response({
            "message": "Заказ изменен",
        })

    def patch(self, request, pk=None):
        return Response({
            "message": "Заказ изменен",
        })

    def delete(self, request, pk=None):
        return Response(
            {"message": "Заказ удален"},
            status=status.HTTP_204_NO_CONTENT
        )

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='orders')]
