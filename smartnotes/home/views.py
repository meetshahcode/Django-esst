from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Homeview(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today":datetime.today()}


class authorizedview(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"