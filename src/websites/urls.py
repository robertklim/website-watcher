from django.urls import path
from .views import WebsitesListView

app_name = 'websites'

urlpatterns = [
    path('', WebsitesListView.as_view(), name='websites-list'),
]
