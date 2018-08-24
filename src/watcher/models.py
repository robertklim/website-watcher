from django.db import models
from websites.models import Website

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
