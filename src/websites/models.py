from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class Website(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=128)
    url         = models.CharField(max_length=2000)
    description = models.CharField(max_length=1024)
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('websites:website-update', kwargs={'pk': self.pk})
