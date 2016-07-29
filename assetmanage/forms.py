from django import forms

from .models import Asset, AssetTest, ImageAsset


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ("fichier", "file_md5", "type", "status", "project", "provider")


class AssetTestForm(forms.ModelForm):

    class Meta:
        model = AssetTest
        fields = ("file_path", )


class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageAsset
        fields = ("provider", "project", "thumbnail", "itunes", "sasktel")
