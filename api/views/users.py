from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.permissions import CanAccessObject, IsOwner
from api.serializers.users import UserRegisterSerializer, UserSerializer, ChangePasswordSerializer
from users.models import User, Role


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
