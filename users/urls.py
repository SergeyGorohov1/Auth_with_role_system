from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from users.apps import UsersConfig
from users.forms import CustomAuthenticationForm
from users.views import RegisterView, logout_view

app_name = UsersConfig.name

urlpatterns = [
    # url-адреса входа и выхода
    path("login/", LoginView.as_view(template_name="users/login.html", form_class=CustomAuthenticationForm), name="login"),
    path("logout/", logout_view, name="logout"),


    # url-адреса смены пароля
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("register/", RegisterView.as_view(), name="register"),
    #path("edit/", edit, name="edit"),
]
