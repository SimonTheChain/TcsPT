from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from projectmanage.models import Provider, Project
import os


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


class AssetTest(models.Model):
    file_path = models.FilePathField(path=r"C:\Users\Simon\Pictures\poster_arts", default="")

    def __str__(self):
        return self.file_path


class Asset(models.Model):
    file_md5 = models.CharField(max_length=32, default="", blank=True)
    type = models.CharField(max_length=25, choices=ASSET_TYPES, default="feature")
    status = models.CharField(max_length=25, choices=ASSET_STATUS, default="datadownready")
    fichier = models.FileField(default="")
    project = models.ForeignKey(Project, blank=True, null=True)  # on_delete=models.CASCADE
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def filename(self):
        return os.path.basename(self.fichier.name)

    def __str__(self):
        return os.path.basename(self.fichier.name)


class ImageAsset(models.Model):
    thumbnail = ProcessedImageField(
        upload_to="media/thumbnails/%Y/%m/%d/",
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60})
    itunes = ProcessedImageField(upload_to="media/itunes/%Y/%m/%d/", processors=[ResizeToFill(2000, 3000)], format='JPEG',
                                    options={'quality': 100})
    sasktel = ProcessedImageField(upload_to="media/sasktel/%Y/%m/%d/", processors=[ResizeToFill(160, 229)], format='JPEG',
                                 options={'quality': 100})
    project = models.ForeignKey(Project, blank=True, null=True)  # on_delete=models.CASCADE
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def filename(self):
        return os.path.basename(self.thumbnail.name)

    def __str__(self):
        return os.path.basename(self.thumbnail.name)
