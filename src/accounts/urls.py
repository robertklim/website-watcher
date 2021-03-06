from django.urls import path

from .views import (
    AccountCreateView,
    AccountProfileView,
    AccountUpdateView,
    # account_edit,
)

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('profile/', AccountProfileView.as_view(), name='account-profile'),
    path('profile/edit/', AccountUpdateView.as_view(), name='account-edit'),
]
