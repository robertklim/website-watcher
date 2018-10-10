from django import forms
from .models import Website, WebsiteCheckSettings

class WebsiteCreateForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = [
            'name',
            'url',
            'description',
        ]

class WebsiteCheckSettingsCreateForm(forms.ModelForm):
    class Meta:
        model = WebsiteCheckSettings
        fields = [
            'dom_exclusions',
        ]