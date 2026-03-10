from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.forms import CustomAuthenticationForm
from users.views import (PasswordChangeMeView, PermissionsCreateView,
                         PermissionsDeleteView, PermissionsListView,
                         PermissionsUpdateView, RegisterView, RoleCreateView,
                         RoleDeleteView, RoleListView, RoleUpdateView,
                         UserDeleteMeView, UserDeleteView, UserListView,
                         UserUpdateMeView, UserUpdateView, logout_view)

app_name = UsersConfig.name

urlpatterns = [
    # url-адреса входа и выхода
    path("login/", LoginView.as_view(template_name="users/login.html", form_class=CustomAuthenticationForm),
         name="login"),
    path("logout/", logout_view, name="logout"),

    # url-адреса смены пароля
    path("password-change/", PasswordChangeMeView.as_view(template_name="users/password_change_form.html"),
         name="password_change"),

    path("register/", RegisterView.as_view(), name="register"),
    path("my_profile/edit/", UserUpdateMeView.as_view(), name="edit"),
    path("my_profile/disable/", UserDeleteMeView.as_view(), name="delete"),

    path('users/', UserListView.as_view(), name='users_list'),
    path('users/create/', RegisterView.as_view(), name='users_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete'),

    path('roles/', RoleListView.as_view(), name='roles_list'),
    path('roles/create/', RoleCreateView.as_view(), name='roles_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='roles_update'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='roles_delete'),

    path('permissions/', PermissionsListView.as_view(), name='permissions_list'),
    path('permissions/create/', PermissionsCreateView.as_view(), name='permissions_create'),
    path('permissions/<int:pk>/update/', PermissionsUpdateView.as_view(), name='permissions_update'),
    path('permissions/<int:pk>/delete/', PermissionsDeleteView.as_view(), name='permissions_delete'),
]
