from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import UserRegisterApiView, UserRetrieveUpdateDestroyApiView, UserChangePasswordApiView, RoleViewSet, \
    ElementViewSet, UserListApiView, UserRetrieveUpdateDestroyOtherUsersApiView

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'elements', ElementViewSet, basename='elements')


urlpatterns = [
    path("register/", UserRegisterApiView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', UserListApiView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyOtherUsersApiView.as_view()),
    path('users/me/', UserRetrieveUpdateDestroyApiView.as_view()),
    path('users/me/change_password/', UserChangePasswordApiView.as_view()),

    path('', include(router.urls)),
]
