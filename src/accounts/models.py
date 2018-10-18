from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    name            = models.CharField(max_length=32, blank=True)
    surname         = models.CharField(max_length=32, blank=True)
    phone_number    = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'