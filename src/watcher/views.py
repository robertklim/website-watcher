from bs4 import BeautifulSoup

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from websites.models import Website

from .forms import WebsiteCheckSettingsCreateForm
from .models import Check, WebsiteCheck, WebsiteCheckSettings

import hashlib
import re
import requests

class WebsiteCheckSettingsListView(ListView):
    pk_url_kwargs = 'website_pk'

    def get_queryset(self):
        return WebsiteCheckSettings.objects.filter(website=self.kwargs.get('website_pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_pk'] = self.kwargs.get('website_pk')
        context['website'] = Website.objects.get(pk=context['website_pk'])
        return context

class WebsiteCheckSettingsDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(WebsiteCheckSettings, pk=self.kwargs.get('website_settings_pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checks'] = WebsiteCheck.objects.filter(website_settings=self.kwargs.get('website_settings_pk'))
        return context

class WebsiteCheckSettingsCreateView(CreateView):
    form_class = WebsiteCheckSettingsCreateForm
    template_name = 'watcher/websitechecksettings_create.html'
    pk_url_kwargs = 'website_pk'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.website = Website.objects.get(
            pk=self.kwargs.get('website_pk'))
        return super(WebsiteCheckSettingsCreateView, self).form_valid(form)

class WebsiteCheckSettingsUpdateView(UpdateView):
    form_class = WebsiteCheckSettingsCreateForm
    template_name = 'watcher/websitechecksettings_update.html'
    pk_url_kwarg = 'website_settings_pk'

    def get_queryset(self):
        return WebsiteCheckSettings.objects.filter(website=self.kwargs.get('website_pk'))

class WebsiteCheckSettingsDeleteView(DeleteView):
    model = WebsiteCheckSettings
    pk_url_kwarg = 'website_settings_pk'
    # success_url = reverse_lazy('websites:website-list')

    def get_success_url(self):
        website_pk = self.object.website.pk
        return reverse_lazy('watcher:website-settings-list', kwargs={'website_pk': website_pk})

class WebsiteCheckListView(ListView):
    paginate_by = 6

    def get_queryset(self):
        return WebsiteCheck.objects.filter(website_settings=self.kwargs.get('website_settings_pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_check_settings'] = WebsiteCheckSettings.objects.get(pk=self.kwargs.get('website_settings_pk'))
        return context

class WebsiteCheckSettingsGenerateHashView(View):
    def get(self, request, website_pk, website_settings_pk):
        website_pk = self.kwargs.get('website_pk')
        website_settings_pk = self.kwargs.get('website_settings_pk')
        website_check_settings = WebsiteCheckSettings.objects.get(pk=website_settings_pk)
        website_url = website_check_settings.website.url

        try:
            source = requests.get(website_url).text
        except requests.exceptions.RequestException as e:
            print(e)
            source = None

        if source is not None:
            soup = BeautifulSoup(source, 'lxml')
            
            for exclusion in website_check_settings.dom_exclusions.names():
                # regex = r'^[\w*]-?[_a-zA-Z]+[_a-zA-Z0-9-]*|[\W]-?[_a-zA-Z]+[_a-zA-Z0-9-]*'
                # test = re.findall(regex, exclusion)
                # exclusion_components = re.findall(regex, exclusion)

                for element in soup.select(exclusion):
                    element.decompose()
                    
            website_hash = hashlib.md5(str(soup).encode('utf-8')).hexdigest()
        else:
            website_hash = ''

        website_check_settings.website_hash = website_hash
        website_check_settings.save()

        return redirect('watcher:website-settings-detail', website_pk=website_pk, website_settings_pk=website_settings_pk)

class WebsiteCheckView(View):
    def get(self, request, website_pk, website_settings_pk):
        website_pk = self.kwargs.get('website_pk')
        website_settings_pk = self.kwargs.get('website_settings_pk')
        website_check_settings = WebsiteCheckSettings.objects.get(pk=website_settings_pk)
        website_url = website_check_settings.website.url
        website_hash = website_check_settings.website_hash
        result = None
        error = None

        try:
            source = requests.get(website_url).text
        except requests.exceptions.RequestException as e:
            print(e)
            source = None
            result = 'ERROR'
            error = e

        if source is not None:
            soup = BeautifulSoup(source, 'lxml')
            
            # Set defaults
            html_element = 'div'
            html_attribute = 'class'
            html_attribute_value = ''
            for exclusion in website_check_settings.dom_exclusions.names():
                # class found
                if re.search('\.', exclusion) is not None:
                    html_attribute = 'class'
                # id found
                if re.search('#', exclusion) is not None:
                    html_attribute = 'id'
                
                # split exclusion to html_element part and html_attribute_value
                exclusion_components = re.split('#|\.', exclusion)

                # check number of components
                if len(exclusion_components) < 2:
                    html_attribute_value = exclusion_components[0]
                elif len(exclusion_components) == 2:
                    if exclusion_components[0] != '':
                        html_element = exclusion_components[0]
                    html_attribute_value = exclusion_components[1]

                for element in soup.find_all(html_element, {html_attribute: html_attribute_value}):
                    element.decompose()
                    # Reset defaults
                    html_element = 'div'
                    html_attribute = 'class'
                    html_attribute_value = ''
            
            check_hash = hashlib.md5(str(soup).encode('utf-8')).hexdigest()
            if website_hash == check_hash:
                result = 'OK'
            else:
                result = 'ALERT'
        else:
            check_hash = ''
            result = 'ERROR'
            error = 'NO CHECK HASH'

        WebsiteCheck.objects.create(
            website_settings=website_check_settings,
            check_hash=check_hash,
            result=result,
            error=error,
        ).save()

        return redirect('watcher:website-settings-detail', website_pk=website_pk, website_settings_pk=website_settings_pk)

def check_user_websites(request):
    user = request.user
    websites = Website.objects.filter(user=user)
    for website in websites:
        check_website(request, website.pk)
    return redirect('/websites')

def check_website(request, website_pk):
    website = Website.objects.get(pk=website_pk)
    website_url = website.url
    try:
        source = requests.get(website_url).text
    except requests.exceptions.RequestException as e:
        print(e)
        source = None
    
    if source is not None:
        soup = BeautifulSoup(source, 'lxml')
        website_hash = hashlib.md5(str(soup).encode('utf-8')).hexdigest()
    else:
        website_hash = ''

    try:
        last_check = Check.objects.filter(website_url=website_url).latest()
    except Check.DoesNotExist:
        last_check = None

    if last_check is not None and website_hash != '':
        result = 'ok' if last_check.website_hash == website_hash else 'err'
    elif website_hash == '':
        result = 'con err'
    else:
        result = 'first check'

    Check.objects.create(
        website = website,
        website_url = website_url,
        website_hash = website_hash,
        result = result,
    ).save()

    return redirect('/websites')


