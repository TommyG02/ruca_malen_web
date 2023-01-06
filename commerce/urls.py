from django.urls import path

from commerce.views import bienvenidos

urlpatterns = [
    path('bienvenidos/', bienvenidos),
]