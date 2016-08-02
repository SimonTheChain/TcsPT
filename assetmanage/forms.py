from django import forms

from .models import Video, Audio, Subtitle, Image, Note


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = [
            "project",
            "type",
            "file_name",
            "file_path",
            "file_size",
            "file_md5",
            "locale",
            "format",
            "crop_top",
            "crop_bottom",
            "crop_right",
            "crop_left",
            "status"
        ]
