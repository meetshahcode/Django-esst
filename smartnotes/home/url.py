from django.urls import path

from . import views

urlpatterns = [
    path("",views.Homeview.as_view(),name = "home"),
    path("authorized",views.authorizedview.as_view(),name = "authorized"),
    path("login",views.LoginInterfaceView.as_view(),name = "login"),
    path("logout",views.LogoutInterfaceView.as_view(),name = "logout"),
    path("signup",views.SignupView.as_view(),name = "signup"),
]