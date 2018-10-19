from django import forms
from .models import Website

class WebsiteCreateForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = [
            'name',
            'url',
            'description',
        ]