from django.contrib import admin
from django.urls import path
from shop.api import api
from shop.views import products_django

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("products-django/", products_django),
]