from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import UserRegisterApiView, UserRetrieveUpdateDestroyApiView

urlpatterns = [
    path("register/", UserRegisterApiView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/me/', UserRetrieveUpdateDestroyApiView.as_view()),
]
