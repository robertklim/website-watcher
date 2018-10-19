from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    View,
)

from .forms import (
    AccountCreateForm,
    UserUpdateForm,
    ProfileUpdateForm,
)

class AccountCreateView(CreateView):
    form_class = AccountCreateForm
    template_name = 'accounts/account_create_form.html'

    def get_success_url(self):
        return reverse_lazy('login')

class AccountProfileView(View):
    template_name = 'accounts/account_profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

def account_edit(request):
    if (request.method == 'POST'):
        usr_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if usr_form.is_valid() and prof_form.is_valid():
            usr_form.save()
            prof_form.save()
            return redirect('accounts:account-profile')
    else:
        usr_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'usr_form': usr_form,
        'prof_form': prof_form,
    }

    return render(request, 'accounts/account_update_form.html', context)