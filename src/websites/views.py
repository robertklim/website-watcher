from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Website

class WebsiteListView(ListView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteDetailView(DetailView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)