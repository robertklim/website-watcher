from django.conf import settings
from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager

User = settings.AUTH_USER_MODEL

class Website(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=128)
    url         = models.CharField(max_length=2000)
    description = models.CharField(max_length=1024)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('websites:website-detail', kwargs={'pk': self.pk})

class WebsiteCheckSettings(models.Model):
    website         = models.ForeignKey(Website, on_delete=models.CASCADE)
    website_hash    = models.CharField(max_length=128)
    dom_exclusions  = TaggableManager(blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website.name + ' settings'

    def get_absolute_url(self):
        website_check_settings = WebsiteCheckSettings.objects.get(pk=self.pk)
        return reverse('websites:website-settings-detail', kwargs={'pk': website_check_settings.website.pk, 'website_settings_pk': self.pk})
