from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.permissions import CanAccessObject, IsOwner
from elements.models import Element

from users.models import User, Role, AccessRolesRules

from api.serializers import UserRegisterSerializer, UserSerializer, ChangePasswordSerializer, RoleSerializer, \
    ElementSerializer, AccessRolesRulesSerializer


class UserRegisterApiView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        role = Role.objects.get_or_create(name="user")[0]  # У зарег. пользователя, по умолчанию право user
        user.role = role
        user.save()


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='users')]


class UserRetrieveUpdateDestroyOtherUsersApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [IsAuthenticated(), IsOwner() or CanAccessObject(object='users')]

    def delete(self, request, *args, **kwargs):
        user = self.get_object()

        user.is_active = False
        user.save()

        return Response({"detail": "Пользователь удален"}, status=status.HTTP_204_NO_CONTENT)


class UserRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()

        user.is_active = False
        user.save()

        return Response({"detail": "Пользователь удален"}, status=status.HTTP_204_NO_CONTENT)


class UserChangePasswordApiView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Пароль успешно изменён"}, status=status.HTTP_200_OK)


class AccessRolesRulesViewSet(ModelViewSet):
    queryset = AccessRolesRules.objects.all()
    serializer_class = AccessRolesRulesSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='permissions')]


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='roles')]


class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='elements')]


class ProductsView(APIView):

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
            {"message": f"Продукт удален"},
            status=status.HTTP_204_NO_CONTENT
        )

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='products')]


class OrdersView(APIView):

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
            {"message": f"Заказ удален"},
            status=status.HTTP_204_NO_CONTENT
        )

    def get_permissions(self):
        return [IsAuthenticated(), CanAccessObject(object='orders')]
