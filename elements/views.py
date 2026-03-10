from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from elements.forms import ElementForm
from users.permissions import can_access_object

from elements.models import Element


def home(request):
    elements = Element.objects.all()
    return render(request, "home.html", {"elements": elements})


class ElementsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Element
    template_name = "list.html"
    extra_context = {"name": "Элементы"}


    def test_func(self):
        return can_access_object(self.request, "elements")


class ElementsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Element
    form_class = ElementForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Элемент"}

    def test_func(self):
        return can_access_object(self.request, "elements")


class ElementsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Element
    form_class = ElementForm
    success_url = reverse_lazy("elements:home")
    template_name = "form.html"
    extra_context = {"name": "Элемент"}

    def test_func(self):
        return can_access_object(self.request, "elements")


class ElementsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Element
    success_url = reverse_lazy("elements:home")
    template_name = "confirm_delete.html"
    extra_context = {"name": "Элемент"}

    def test_func(self):
        return can_access_object(self.request, "elements")
