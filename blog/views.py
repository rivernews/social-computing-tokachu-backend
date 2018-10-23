from django.shortcuts import render

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

home_view = HomeView.as_view()