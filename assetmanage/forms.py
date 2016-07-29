from django import forms

from .models import Asset


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ("file_name", "file_path", "file_size", "file_md5", "type", "status", "project", "provider",)
