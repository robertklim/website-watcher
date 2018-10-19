from django import forms
from .models import WebsiteCheckSettings

class WebsiteCheckSettingsCreateForm(forms.ModelForm):
    class Meta:
        model = WebsiteCheckSettings
        fields = [
            'dom_exclusions',
        ]
