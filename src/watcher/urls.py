from django.urls import path
from .views import (
    check_website,
)

app_name = 'watcher'

urlpatterns = [
     path('check/<int:website_pk>', check_website, name='watcher-check'),
]
