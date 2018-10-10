from django.urls import path
from .views import (
    WebsiteCreateView,
    WebsiteDeleteView, 
    WebsiteDetailView, 
    WebsiteListView, 
    WebsiteUpdateView,
    WebsiteCheckSettingsCreateView,
    WebsiteCheckSettingsDetailView,
    WebsiteCheckSettingsListView,
)

app_name = 'websites'

urlpatterns = [
    path('', WebsiteListView.as_view(), name='website-list'),
    path('<int:pk>/', WebsiteDetailView.as_view(), name='website-detail'),
    path('<int:pk>/update/', WebsiteUpdateView.as_view(), name='website-update'),
    path('<int:pk>/delete/', WebsiteDeleteView.as_view(), name='website-delete'),
    path('create/', WebsiteCreateView.as_view(), name='website-create'),
    path('<int:pk>/settings/', WebsiteCheckSettingsListView.as_view(), name='website-settings-list'),
    path('<int:pk>/settings/<int:website_settings_pk>/', WebsiteCheckSettingsDetailView.as_view(), name='website-settings-detail'),
    path('<int:pk>/settings/create/', WebsiteCheckSettingsCreateView.as_view(), name='website-settings-create'),
]
