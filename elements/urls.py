from django.urls import path

from elements.views import home, ElementsListView, ElementsCreateView, ElementsUpdateView, ElementsDeleteView
from elements.apps import ElementsConfig

app_name = ElementsConfig.name

urlpatterns = [
    path('', home, name='home'),

    path('elements/', ElementsListView.as_view(), name='elements_list'),
    path('elements/create/', ElementsCreateView.as_view(), name='elements_create'),
    path('elements/<int:pk>/update/', ElementsUpdateView.as_view(), name='elements_update'),
    path('elements/<int:pk>/delete/', ElementsDeleteView.as_view(), name='elements_delete'),

    # path('products/', ElementsListView.as_view(), name='products_list'),
    # path('products/create/', ElementsListView.as_view(), name='products_create'),
    # path('products/<int:pk>/update/', ElementsListView.as_view(), name='products_update'),
    # path('products/<int:pk>/delete/', ElementsListView.as_view(), name='products_delete'),
    #
    # path('orders/', ElementsListView.as_view(), name='orders_list'),
    # path('orders/create/', ElementsListView.as_view(), name='orders_create'),
    # path('orders/<int:pk>/update/', ElementsListView.as_view(), name='orders_update'),
    # path('orders/<int:pk>/delete/', ElementsListView.as_view(), name='orders_delete'),
]
