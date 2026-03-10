from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from elements.views import ElementsListView
from users.apps import UsersConfig
from users.forms import CustomAuthenticationForm
from users.views import RegisterView, logout_view, RoleCreateView, RoleListView, RoleUpdateView, RoleDeleteView, \
    PermissionsCreateView, PermissionsDeleteView, PermissionsUpdateView, PermissionsListView

app_name = UsersConfig.name

urlpatterns = [
    # url-адреса входа и выхода
    path("login/", LoginView.as_view(template_name="users/login.html", form_class=CustomAuthenticationForm),
         name="login"),
    path("logout/", logout_view, name="logout"),

    # url-адреса смены пароля
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("register/", RegisterView.as_view(), name="register"),
    # path("edit/", edit, name="edit"),

    path('roles/', RoleListView.as_view(), name='elements_list'),
    path('roles/create/', RoleCreateView.as_view(), name='elements_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='elements_update'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='elements_delete'),

    path('permissions/', PermissionsListView.as_view(), name='elements_list'),
    path('permissions/create/', PermissionsCreateView.as_view(), name='elements_create'),
    path('permissions/<int:pk>/update/', PermissionsUpdateView.as_view(), name='elements_update'),
    path('permissions/<int:pk>/delete/', PermissionsDeleteView.as_view(), name='elements_delete'),
]
