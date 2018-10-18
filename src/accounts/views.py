from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
)

from .forms import AccountCreateForm

class AccountCreateView(CreateView):
    form_class = AccountCreateForm
    template_name = 'accounts/account_create_form.html'

    def get_success_url(self):
        return reverse_lazy('login')
