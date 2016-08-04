from django.db import models
from django.core.urlresolvers import reverse
from projectmanage.models import Project
from metadata.models import Metadata


VIDEO_TYPES = (
            ("feature", "Feature"),
            ("trailer", "Trailer"),
            ("preview", "Preview"),
)


AUDIO_TYPES = (
            ("feataltaudio", "Feature Alternate Audio"),
            ("featdesaudio", "Feature Descriptive Audio"),
            ("trailaltaudio", "Trailer Alternate Audio"),
            ("prevaltaudio", "Preview Alternate Audio"),
)


SUBTITLE_TYPES = (
            ("featscc", "Feature CC"),
            ("featitt", "Feature ITT"),
            ("featsrt", "Feature SRT"),
            ("trailscc", "Trailer CC"),
            ("trailitt", "Trailer ITT"),
            ("trailsrt", "Trailer SRT"),
            ("prevscc", "Preview CC"),
            ("previtt", "Preview ITT"),
            ("prevsrt", "Preview SRT"),
)


IMAGE_TYPES = (
            ("posteritunes", "iTunes Poster Art"),
            ("postergoogle", "Google Poster Art"),
            ("postersasktel", "Sasktel Poster Art"),
            ("posternetflix", "Netflix Poster Art"),
            ("posteramazon", "Amazon Poster Art"),
            ("postermicro", "Microsoft Poster Art"),
)


NOTE_TYPES = (
        ("qcreport", "Qc report"),
        ("baton", "Baton report"),
)


ASSET_STATUS = (
        ("active", "Active"),
        ("archived", "Archived"),
    )


FORMAT_TYPES = (
    ("hd", "HD"),
    ("sd", "SD"),
)


AUDIO_CHANNELS = (
        ("noaudio", "Not used"),
        ("audioleft", "Left"),
        ("audioright", "Right"),
        ("audiocenter", "Center"),
        ("audiolfe", "L.F.E."),
        ("audiobackleft", "Surround left"),
        ("audiobackright", "Surround Right"),
        ("audiolefttotal", "Left total"),
        ("audiorighttotal", "Right total"),
        ("audiomono", "Mono"),
    )


LOCALES = (
        ("enca", "en-CA"),
        ("enus", "en-US"),
        ("frca", "fr-CA"),
        ("frfr", "fr-FR"),
    )


class Video(models.Model):
    file_name = models.CharField(max_length=250, default="")
    file_path = models.CharField(max_length=250, default="", blank=True)
    file_size = models.IntegerField(default=0, blank=True)
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    locale = models.CharField(max_length=25, choices=LOCALES, default="enus")
    format = models.CharField(max_length=25, choices=FORMAT_TYPES, default="hd")
    crop_top = models.IntegerField(default=4)
    crop_bottom = models.IntegerField(default=4)
    crop_right = models.IntegerField(default=4)
    crop_left = models.IntegerField(default=4)
    type = models.CharField(max_length=25, choices=VIDEO_TYPES, default="feature")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="active")
    metadata = models.ForeignKey(Metadata, default=1, related_name="video_set")
    project = models.ForeignKey(Project, default=1)

    def get_absolute_url(self):
        return reverse("assetmanage:video_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.file_name


class Audio(models.Model):
    file_name = models.CharField(max_length=250, default="")
    file_path = models.CharField(max_length=250, default="", blank=True)
    file_size = models.IntegerField(default=0, blank=True)
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    locale = models.CharField(max_length=25, choices=LOCALES, default="enus")
    channel_1 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_2 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_3 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_4 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_5 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_6 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_7 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_8 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    type = models.CharField(max_length=25, choices=AUDIO_TYPES, default="feature")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="active")
    project = models.ForeignKey(Project, default=1)

    def get_absolute_url(self):
        return reverse("assetmanage:audio_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.file_name


class Subtitle(models.Model):
    file_name = models.CharField(max_length=250, default="")
    file_path = models.CharField(max_length=250, default="", blank=True)
    file_size = models.IntegerField(default=0, blank=True)
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    type = models.CharField(max_length=25, choices=SUBTITLE_TYPES, default="featscc")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="active")
    locale = models.CharField(max_length=25, choices=LOCALES, default="enus")
    project = models.ForeignKey(Project, default=1)

    def get_absolute_url(self):
        return reverse("assetmanage:subtitle_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.file_name


class Image(models.Model):
    file_name = models.CharField(max_length=250, default="")
    file_path = models.CharField(max_length=250, default="", blank=True)
    file_size = models.IntegerField(default=0, blank=True)
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    type = models.CharField(max_length=25, choices=IMAGE_TYPES, default="posteritunes")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="active")
    width = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    project = models.ForeignKey(Project, default=1)

    # def get_absolute_url(self):
    #     return reverse("assetmanage:image_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.file_name


class Note(models.Model):
    file_name = models.CharField(max_length=250, default="")
    file_path = models.CharField(max_length=250, default="", blank=True)
    file_size = models.IntegerField(default=0, blank=True)
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    type = models.CharField(max_length=25, choices=NOTE_TYPES, default="qcreport")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="active")
    project = models.ForeignKey(Project, default=1)

    # def get_absolute_url(self):
    #     return reverse("assetmanage:note_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.file_name
