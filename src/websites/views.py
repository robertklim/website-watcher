from django.shortcuts import render
from django.views.generic import ListView
from .models import Website

class WebsitesListView(ListView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)
