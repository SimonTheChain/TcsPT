from django.db import models
from django.core.urlresolvers import reverse
from datetime import date

from projectmanage.models import Provider, Project


class MetadataMain(models.Model):
    studio_release_title = models.CharField(max_length=250, default="")
    release_date = models.DateField(default=date.today, blank=True, null=True)
    production_company = models.CharField(max_length=250, default="", blank=True, null=True)
    project = models.OneToOneField(Project)  # on_delete=models.CASCADE
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.studio_release_title


class MetadataEN(models.Model):
    title = models.CharField(max_length=250, default="")
    synopsis_long = models.CharField(max_length=1000, default="", blank=True, null=True)
    synopsis_short = models.CharField(max_length=250, default="", blank=True, null=True)
    metadata_main = models.OneToOneField(MetadataMain, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class MetadataFR(models.Model):
    title = models.CharField(max_length=250, default="")
    synopsis_long = models.CharField(max_length=1000, default="", blank=True, null=True)
    synopsis_short = models.CharField(max_length=250, default="", blank=True, null=True)
    metadata_main = models.OneToOneField(MetadataMain, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class MetadataItunes(models.Model):
    est_start_date = models.DateField(default=date.today, blank=True, null=True)
    est_end_date = models.DateField(default=date.today, blank=True, null=True)
    vod_start_date = models.DateField(default=date.today, blank=True, null=True)
    vod_end_date = models.DateField(default=date.today, blank=True, null=True)
    sd_price_tier = models.IntegerField(default=0)
    hd_price_tier = models.IntegerField(default=0)
    metadata_main = models.OneToOneField(MetadataMain, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.metadata_main.studio_release_title


class MetadataSasktel(models.Model):
    license_start_date = models.DateField(default=date.today, blank=True, null=True)
    license_end_date = models.DateField(default=date.today, blank=True, null=True)
    sasktel_rating = models.CharField(max_length=10, default="", blank=True, null=True)
    sd_price = models.FloatField(default=0)
    hd_price = models.FloatField(default=0)
    metadata_main = models.OneToOneField(MetadataMain, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.metadata_main.studio_release_title


class CastCrew(models.Model):
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    apple_id = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.first_name + self.last_name
