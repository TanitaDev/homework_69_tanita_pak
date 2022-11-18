from django.contrib import admin
from django.urls import path

from webapp.views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide'),
]
