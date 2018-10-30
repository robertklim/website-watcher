from django.db import models
from django.urls import reverse

from websites.models import Website

from taggit.managers import TaggableManager

CHECK_RESULTS = (
    ('OK', 'Ok'),
    ('ALERT', 'Alert'),
    ('ERROR', 'Error'),
    (None, 'None'),
)

class Check(models.Model):
    website         = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='checks')
    website_url     = models.CharField(max_length=2000)
    website_hash    = models.CharField(max_length=128)
    result          = models.CharField(max_length=32)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website_url

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']

class WebsiteCheckSettings(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    website_hash = models.CharField(max_length=128)
    dom_exclusions = TaggableManager(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website.name + ' settings'

    def get_absolute_url(self):
        website_check_settings = WebsiteCheckSettings.objects.get(pk=self.pk)
        return reverse('watcher:website-settings-detail', kwargs={'website_pk': website_check_settings.website.pk, 'website_settings_pk': self.pk})

class WebsiteCheck(models.Model):
    website_settings    = models.ForeignKey(WebsiteCheckSettings, on_delete=models.CASCADE, related_name='website_checks')
    check_hash          = models.CharField(max_length=128)
    result              = models.CharField(max_length=128, choices=CHECK_RESULTS, blank=True)
    error               = models.CharField(max_length=128, blank=True, null=True)
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website_settings.website.name + ' check'

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']
