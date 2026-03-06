from django.urls import path
from api.views import UserRegisterApiView

urlpatterns = [
    path("register/", UserRegisterApiView.as_view())
]
