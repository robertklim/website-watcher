from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DeleteView, 
    DetailView, 
    ListView, 
    UpdateView,
)
from .forms import WebsiteCreateForm, WebsiteCheckSettingsCreateForm
from .models import Website, WebsiteCheckSettings

class WebsiteCheckSettingsListView(ListView):
    pk_url_kwargs = 'website_pk'
    def get_queryset(self):
        return WebsiteCheckSettings.objects.filter(website=self.kwargs.get('website_pk'))

class WebsiteCheckSettingsDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(WebsiteCheckSettings, pk=self.kwargs.get('website_settings_pk'))

class WebsiteCheckSettingsCreateView(CreateView):
    form_class = WebsiteCheckSettingsCreateForm
    template_name = 'websites/websitechecksettings_create.html'
    pk_url_kwargs = 'website_pk'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.website = Website.objects.get(pk=self.kwargs.get('website_pk'))
        return super(WebsiteCheckSettingsCreateView, self).form_valid(form)

class WebsiteCheckSettingsUpdateView(UpdateView):
    form_class = WebsiteCheckSettingsCreateForm
    template_name = 'websites/websitechecksettings_update.html'
    pk_url_kwarg = 'website_settings_pk'

    def get_queryset(self):
        return WebsiteCheckSettings.objects.filter(website=self.kwargs.get('website_pk'))

class WebsiteCheckSettingsDeleteView(DeleteView):
    model = WebsiteCheckSettings
    pk_url_kwarg = 'website_settings_pk'
    # success_url = reverse_lazy('websites:website-list')

    def get_success_url(self):
        website_pk = self.object.website.pk
        return reverse_lazy('websites:website-settings-list', kwargs={'website_pk': website_pk})

class WebsiteListView(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Website.objects.filter(user=self.request.user)
        return Website.objects.none()

class WebsiteDetailView(DetailView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteCreateView(CreateView):
    form_class = WebsiteCreateForm
    template_name = 'websites/website_create.html'
    # success_url = reverse_lazy('websites:website-list')

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
