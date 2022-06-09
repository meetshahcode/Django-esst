from django.urls import path

from . import views

urlpatterns = [
    path("home",views.Homeview.as_view(),name = "home"),
    path("authorized",views.authorizedview.as_view(),name = "authorized")
]