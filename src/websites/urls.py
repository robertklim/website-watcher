from django.urls import path
from .views import (
    WebsiteCreateView,
    WebsiteDeleteView, 
    WebsiteDetailView, 
    WebsiteListView, 
    WebsiteUpdateView,
)

app_name = 'websites'

urlpatterns = [
    path('', WebsiteListView.as_view(), name='website-list'),
    path('<int:pk>', WebsiteDetailView.as_view(), name='website-detail'),
    path('<int:pk>/update/', WebsiteUpdateView.as_view(), name='website-update'),
    path('<int:pk>/delete/', WebsiteDeleteView.as_view(), name='website-delete'),
    path('create/', WebsiteCreateView.as_view(), name='website-create'),
]
