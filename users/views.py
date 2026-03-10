from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from users.forms import UserRegisterForm, RoleForm, AccessRolesRulesForm, UserUpdateForm
from users.models import User, Role, AccessRolesRules
from users.permissions import can_access_object


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        role = Role.objects.get_or_create(name="user")[0]  # У зарег. пользователя, по умолчанию право user
        form.instance.role = role
        messages.success(self.request, 'Регистрация прошла успешно!')
        return super().form_valid(form)


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = "list.html"
    extra_context = {"name": "Пользователи", "url_name": "users"}

    def test_func(self):
        return can_access_object(self.request, "users")


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Пользователь"}

    def test_func(self):
        return can_access_object(self.request, "users")


class UserUpdateMeView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Пользователь"}

    def get_object(self, queryset=None):
        return self.request.user


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy("elements:home")
    template_name = "confirm_delete.html"
    extra_context = {"name": "Пользователь", "url_name": "users"}

    def test_func(self):
        return can_access_object(self.request, "users")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class UserDeleteMeView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("elements:home")
    template_name = "confirm_delete.html"
    extra_context = {"name": "Пользователь"}

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


def logout_view(request):
    logout(request)
    return redirect("/")


class RoleListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Role
    template_name = "list.html"
    extra_context = {"name": "Роли", "url_name": "roles"}

    def test_func(self):
        return can_access_object(self.request, "roles")


class RoleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Role
    form_class = RoleForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Роль"}

    def test_func(self):
        return can_access_object(self.request, "roles")


class RoleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Role
    form_class = RoleForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Роль"}

    def test_func(self):
        return can_access_object(self.request, "roles")


class RoleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Role
    success_url = reverse_lazy("elements:home")
    template_name = "confirm_delete.html"
    extra_context = {"name": "Роль", "url_name": "roles"}

    def test_func(self):
        return can_access_object(self.request, "roles")


class PermissionsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = AccessRolesRules
    template_name = "list.html"
    extra_context = {"name": "Права доступа", "url_name": "permissions"}

    def test_func(self):
        return can_access_object(self.request, "permissions")


class PermissionsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AccessRolesRules
    form_class = AccessRolesRulesForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Право доступа"}

    def test_func(self):
        return can_access_object(self.request, "permissions")


class PermissionsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AccessRolesRules
    form_class = AccessRolesRulesForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Право доступа"}

    def test_func(self):
        return can_access_object(self.request, "permissions")


class PermissionsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AccessRolesRules
    success_url = reverse_lazy("elements:home")
    template_name = "confirm_delete.html"
    extra_context = {"name": "Право доступа", "url_name": "permissions"}

    def test_func(self):
        return can_access_object(self.request, "permissions")
