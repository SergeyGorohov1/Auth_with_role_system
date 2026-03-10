from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View)

from elements.forms import ElementForm
from elements.models import Element
from users.permissions import can_access_object


# Контроллеры работы с Элементами
def home(request):
    elements = Element.objects.all()
    return render(request, "home.html", {"elements": elements})


class ElementsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Element
    template_name = "list.html"
    extra_context = {"name": "Элементы", "url_name": "elements"}

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
    extra_context = {"name": "Элемент", "url_name": "elements"}

    def test_func(self):
        return can_access_object(self.request, "elements")


# Контроллеры работы с Продуктами
class ProductsListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "list.html"
    extra_context = {"name": "Продукты", "url_name": "products"}

    def test_func(self):
        return can_access_object(self.request, "products")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()

        context_data["object_list"] = [{"pk": 1, "name": "Продукт 1"}, {"pk": 2, "name": "Продукт 2"},
                                       {"pk": 3, "name": "Продукт 3"}]

        return context_data


class ProductsCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return can_access_object(self.request, "products")

    def get(self, request):
        return HttpResponse('Доступ разрешен')

    def post(self, request):
        return HttpResponse('Доступ разрешен')


class ProductsUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return can_access_object(self.request, "products")

    def get(self, request, pk=None):
        return HttpResponse('Доступ разрешен')

    def put(self, request, pk=None):
        return HttpResponse('Доступ разрешен')


class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return can_access_object(self.request, "products")

    def get(self, request, pk=None):
        return HttpResponse('Доступ разрешен')

    def delete(self, request, pk=None):
        return HttpResponse('Доступ разрешен')


# Контроллеры работы с Заказами
class OrdersListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "list.html"
    extra_context = {"name": "Продукты", "url_name": "orders"}

    def test_func(self):
        return can_access_object(self.request, "orders")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()

        context_data["object_list"] = [{"pk": 1, "name": "Заказ 1"}, {"pk": 2, "name": "Заказ 2"},
                                       {"pk": 3, "name": "Заказ 3"}]

        return context_data


class OrdersCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return can_access_object(self.request, "orders")

    def get(self, request):
        return HttpResponse('Доступ разрешен')

    def post(self, request):
        return HttpResponse('Доступ разрешен')


class OrdersUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return can_access_object(self.request, "orders")

    def get(self, request, pk=None):
        return HttpResponse('Доступ разрешен')

    def put(self, request, pk=None):
        return HttpResponse('Доступ разрешен')


class OrdersDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return can_access_object(self.request, "orders")

    def get(self, request, pk=None):
        return HttpResponse('Доступ разрешен')

    def delete(self, request, pk=None):
        return HttpResponse('Доступ разрешен')
