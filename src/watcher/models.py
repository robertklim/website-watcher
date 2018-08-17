from django.db import models
from websites.models import Website

class Check(models.Model):
    website         = models.ForeignKey(Website, on_delete=models.CASCADE)
    website_hash    = models.CharField(max_length=128)
    result          = models.CharField(max_length=32)
    timestamp       = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.website
