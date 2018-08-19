from django.urls import path
from .views import (
    check_website,
    check_user_websites,
)

app_name = 'watcher'

urlpatterns = [
     path('check/<int:website_pk>', check_website, name='watcher-check'),
     path('check/user/', check_user_websites, name='watcher-check-user-websites'),
]
