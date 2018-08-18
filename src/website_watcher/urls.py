from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('websites/', include('websites.urls', namespace='websites')),
    path('watcher/', include('watcher.urls', namespace='watcher')),
]
