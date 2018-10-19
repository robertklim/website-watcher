from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    View,
)

from .forms import AccountCreateForm

class AccountCreateView(CreateView):
    form_class = AccountCreateForm
    template_name = 'accounts/account_create_form.html'

    def get_success_url(self):
        return reverse_lazy('login')

class AccountProfileView(View):
    template_name = 'accounts/account_profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
