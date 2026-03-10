from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User, Role


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


def logout_view(request):
    logout(request)
    return redirect("/")
