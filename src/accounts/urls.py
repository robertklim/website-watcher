from django.urls import path

from .views import (
    AccountCreateView,
)

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='account-create'),
]
