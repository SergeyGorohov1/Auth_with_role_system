from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.permissions import CanAccessObject, IsOwner
from elements.models import Element

from users.models import User, Role

from api.serializers import UserRegisterSerializer, UserSerializer, ChangePasswordSerializer, RoleSerializer, \
    ElementSerializer


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
