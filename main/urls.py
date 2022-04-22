from django.contrib import admin
from django.urls import path, include
from main.views import all_product

urlpatterns = [
    path('', all_product),
]