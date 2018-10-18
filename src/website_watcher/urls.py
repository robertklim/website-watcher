from django.contrib import admin
from django.urls import path, include
from websites.views import WebsiteListView

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomeView.as_view(), name='home'),
    path('', WebsiteListView.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('websites/', include('websites.urls', namespace='websites')),
    path('watcher/', include('watcher.urls', namespace='watcher')),
    path('', include('django.contrib.auth.urls')),
]
