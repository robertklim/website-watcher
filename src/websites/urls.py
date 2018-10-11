from django.urls import path
from .views import (
    WebsiteCreateView,
    WebsiteDeleteView, 
    WebsiteDetailView, 
    WebsiteListView, 
    WebsiteUpdateView,
    WebsiteCheckSettingsCreateView,
    WebsiteCheckSettingsDeleteView,
    WebsiteCheckSettingsDetailView,
    WebsiteCheckSettingsListView,
    WebsiteCheckSettingsUpdateView,
)

app_name = 'websites'

urlpatterns = [
    path('', WebsiteListView.as_view(), name='website-list'),
    path('create/', WebsiteCreateView.as_view(), name='website-create'),
    path('<int:pk>/', WebsiteDetailView.as_view(), name='website-detail'),
    path('<int:pk>/delete/', WebsiteDeleteView.as_view(), name='website-delete'),
    path('<int:pk>/edit/', WebsiteUpdateView.as_view(), name='website-update'),
    path('<int:website_pk>/settings/', WebsiteCheckSettingsListView.as_view(), name='website-settings-list'),
    path('<int:website_pk>/settings/create/', WebsiteCheckSettingsCreateView.as_view(), name='website-settings-create'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/', WebsiteCheckSettingsDetailView.as_view(), name='website-settings-detail'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/delete/', WebsiteCheckSettingsDeleteView.as_view(), name='website-settings-delete'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/edit/', WebsiteCheckSettingsUpdateView.as_view(), name='website-settings-update'),
]
