from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .forms import WebsiteCreateForm
from .models import Website

class WebsiteListView(ListView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteDetailView(DetailView):
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class WebsiteCreateView(CreateView):
    form_class = WebsiteCreateForm
    template_name = 'websites/website_create.html'
    success_url = '../'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.user = self.request.user
        return super(WebsiteCreateView, self).form_valid(form)