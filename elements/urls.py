from django.urls import path

from elements.apps import ElementsConfig
from elements.views import (ElementsCreateView, ElementsDeleteView,
                            ElementsListView, ElementsUpdateView,
                            OrdersCreateView, OrdersDeleteView, OrdersListView,
                            OrdersUpdateView, ProductsCreateView,
                            ProductsDeleteView, ProductsListView,
                            ProductsUpdateView, home)

app_name = ElementsConfig.name

urlpatterns = [
    path('', home, name='home'),

    path('elements/', ElementsListView.as_view(), name='elements_list'),
    path('elements/create/', ElementsCreateView.as_view(), name='elements_create'),
    path('elements/<int:pk>/update/', ElementsUpdateView.as_view(), name='elements_update'),
    path('elements/<int:pk>/delete/', ElementsDeleteView.as_view(), name='elements_delete'),

    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', ProductsCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductsUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='products_delete'),

    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/create/', OrdersCreateView.as_view(), name='orders_create'),
    path('orders/<int:pk>/update/', OrdersUpdateView.as_view(), name='orders_update'),
    path('orders/<int:pk>/delete/', OrdersDeleteView.as_view(), name='orders_delete'),
]
