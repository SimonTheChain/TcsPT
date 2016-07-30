from django import forms
from collections import OrderedDict
from betterforms.multiform import MultiForm, MultiModelForm

from .models import Asset, Video, Audio, Subtitle, Image, Note


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = (
            "file_name",
            "file_path",
            "file_size",
            "file_md5",
            "type",
            "status",
            "project",
            "provider",
        )


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = (
            "locale",
            "format",
            "crop_top",
            "crop_bottom",
            "crop_right",
            "crop_left",
            "asset",
        )
        exclude = ('asset',)


class AudioForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = (
            "locale",
            "channel_1",
            "channel_2",
            "channel_3",
            "channel_4",
            "channel_5",
            "channel_6",
            "channel_7",
            "channel_8",
            "asset",
        )
        exclude = ('asset',)


class SubtitleForm(forms.ModelForm):

    class Meta:
        model = Subtitle
        fields = (
            "locale",
            "asset",
        )
        exclude = ('asset',)


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = (
            "width",
            "length",
            "asset",
        )
        exclude = ('asset',)


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = (
            "type",
            "comments",
            "asset",
        )
        exclude = ('asset',)


class TestAssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = (
            "file_name",
            "file_path",
            "file_size",
            "file_md5",
            "type",
            "status",
            "project",
            "provider",
        )


class TestVideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = (
            "locale",
            "format",
            "crop_top",
            "crop_bottom",
            "crop_right",
            "crop_left",
            "asset",
        )
        exclude = ('asset',)


class VideoAssetForm(MultiModelForm):
    form_classes = OrderedDict([
        ("asset", TestAssetForm),
        ("video", TestVideoForm),
    ])
