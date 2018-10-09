from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DeleteView, 
    DetailView, 
    ListView, 
    UpdateView,
)
from .forms import WebsiteCreateForm
from .models import Website, WebsiteCheckSettings

class WebsiteCheckSettingsListView(ListView):
    def get_queryset(self):
        return WebsiteCheckSettings.objects.filter(website=self.kwargs.get('pk'))

class WebsiteCheckSettingsDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(WebsiteCheckSettings, pk=self.kwargs.get('website_settings_pk'))

class WebsiteListView(ListView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteDetailView(DetailView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteCreateView(CreateView):
    form_class = WebsiteCreateForm
    template_name = 'websites/website_create.html'
    success_url = reverse_lazy('websites:website-list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.user = self.request.user
        return super(WebsiteCreateView, self).form_valid(form)

class WebsiteUpdateView(UpdateView):
    form_class = WebsiteCreateForm
    template_name = 'websites/website_update.html'

    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteDeleteView(DeleteView):
    model = Website
    success_url = reverse_lazy('websites:website-list')
