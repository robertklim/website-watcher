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
    path('create/', WebsiteCreateView.as_view(), name='website-create'),
    path('<int:pk>/', WebsiteDetailView.as_view(), name='website-detail'),
    path('<int:pk>/delete/', WebsiteDeleteView.as_view(), name='website-delete'),
    path('<int:pk>/edit/', WebsiteUpdateView.as_view(), name='website-update'),
]
