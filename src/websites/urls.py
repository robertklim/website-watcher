from django.urls import path
from .views import WebsiteDetailView, WebsiteListView

app_name = 'websites'

urlpatterns = [
    path('', WebsiteListView.as_view(), name='website-list'),
    path('<int:pk>', WebsiteDetailView.as_view(), name='website-detail'),
]
