from django.urls import path
from .views import (
    WebsiteCheckSettingsCreateView,
    WebsiteCheckSettingsDeleteView,
    WebsiteCheckSettingsDetailView,
    WebsiteCheckSettingsGenerateHashView,
    WebsiteCheckSettingsListView,
    WebsiteCheckSettingsUpdateView,
    WebsiteCheckView,
    check_website,
    check_user_websites,
)

app_name = 'watcher'

urlpatterns = [
    path('check/<int:website_pk>/', check_website, name='watcher-check'),
    path('check/user/', check_user_websites, name='watcher-check-user-websites'),
    path('<int:website_pk>/settings/', WebsiteCheckSettingsListView.as_view(), name='website-settings-list'),
    path('<int:website_pk>/settings/create/', WebsiteCheckSettingsCreateView.as_view(), name='website-settings-create'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/', WebsiteCheckSettingsDetailView.as_view(), name='website-settings-detail'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/delete/', WebsiteCheckSettingsDeleteView.as_view(), name='website-settings-delete'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/edit/', WebsiteCheckSettingsUpdateView.as_view(), name='website-settings-update'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/hashgen/', WebsiteCheckSettingsGenerateHashView.as_view(), name='website-settings-generate-hash'),
    path('<int:website_pk>/settings/<int:website_settings_pk>/check/', WebsiteCheckView.as_view(), name='website-check'),
]
