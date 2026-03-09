from django.urls import path

from elements.views import home
from elements.apps import ElementsConfig

app_name = ElementsConfig.name

urlpatterns = [
    path('', home, name='home')]
