from django.urls import URLPattern, path

from . import views

URLPattern = [
    path("home",views.home,{}),
]