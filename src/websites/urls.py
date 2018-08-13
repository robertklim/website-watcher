from django.urls import path
from .views import WebsiteCreateView, WebsiteDetailView, WebsiteListView

app_name = 'websites'

urlpatterns = [
    path('', WebsiteListView.as_view(), name='website-list'),
    path('<int:pk>', WebsiteDetailView.as_view(), name='website-detail'),
    path('create/', WebsiteCreateView.as_view(), name='website-create'),
]
