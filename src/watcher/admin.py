from django.contrib import admin
from .models import Check, WebsiteCheck, WebsiteCheckSettings

admin.site.register(Check)
admin.site.register(WebsiteCheck)
admin.site.register(WebsiteCheckSettings)
