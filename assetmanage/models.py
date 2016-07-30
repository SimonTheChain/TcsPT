from django.db import models
from django.core.urlresolvers import reverse
from projectmanage.models import Provider, Project


ASSET_TYPES = (
        ("Video", (
            ("feature", "Feature"),
            ("trailer", "Trailer"),
            ("preview", "Preview"),
        )
         ),
        ("Audio", (
            ("feataltaudio", "Feature Alternate Audio"),
            ("featdesaudio", "Feature Descriptive Audio"),
            ("trailaltaudio", "Trailer Alternate Audio"),
            ("prevaltaudio", "Preview Alternate Audio"),
        )
         ),
        ("Subtitle", (
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
         ),
        ("Poster Art", (
            ("posteritunes", "iTunes Poster Art"),
            ("postergoogle", "Google Poster Art"),
            ("postersasktel", "Sasktel Poster Art"),
            ("posternetflix", "Netflix Poster Art"),
            ("posteramazon", "Amazon Poster Art"),
            ("postermicro", "Microsoft Poster Art"),
        )
         ),
        ("Notes", (
            ("qcreport", "Qc Report"),
            ("baton", "Baton Report"),
        )
         ),
    )


ASSET_STATUS = (
        ("Data Wrangling", (
            ("datadownready", "Ready for Download"),
            ("datadownloading", "Downloading"),
            ("datadownloaded", "Downloaded"),
            ("datacopyready", "Ready for Copy"),
            ("datacopyinng", "Copying"),
            ("datacopied", "Copy Done"),
            ("dataupready", "Ready for Upload"),
            ("datauploading", "Uploading"),
            ("datauploaded", "Uploaded"),
            ("dataarchready", "Ready for Archival"),
            ("dataarchiving", "Archiving"),
            ("dataarchived", "Archived"),
        )
         ),
        ("inprod", "In Production"),
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


NOTE_TYPES = (
        ("qcreport", "Qc report"),
        ("baton", "Baton report"),
    )


class Asset(models.Model):
    file_name = models.CharField(max_length=250, default="")
    file_path = models.CharField(max_length=250, default="", blank=True)
    file_size = models.IntegerField(default=0, blank=True)
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    type = models.CharField(max_length=25, choices=ASSET_TYPES, default="feature")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="datadownready")
    project = models.ForeignKey(Project, blank=True, null=True)  # on_delete=models.CASCADE
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.file_name


class Video(models.Model):
    locale = models.CharField(max_length=25, choices=LOCALES, default="")
    format = models.CharField(max_length=25, default="")
    crop_top = models.IntegerField(default=4)
    crop_bottom = models.IntegerField(default=4)
    crop_right = models.IntegerField(default=4)
    crop_left = models.IntegerField(default=4)
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.asset.file_name


class Audio(models.Model):
    locale = models.CharField(max_length=25, choices=LOCALES, default="")
    channel_1 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_2 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_3 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_4 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_5 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_6 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_7 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    channel_8 = models.CharField(max_length=25, choices=AUDIO_CHANNELS, default="noaudio")
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.asset.file_name


class Subtitle(models.Model):
    locale = models.CharField(max_length=25, choices=LOCALES, default="")
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.asset.file_name


class Image(models.Model):
    width = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.asset.file_name


class Note(models.Model):
    type = models.CharField(max_length=25, choices=NOTE_TYPES, default="")
    comments = models.CharField(max_length=1000, default="")
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.asset.file_name
