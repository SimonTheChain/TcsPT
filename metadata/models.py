from django.db import models
from django.core.urlresolvers import reverse
from datetime import date

from projectmanage.models import Project


class Metadata(models.Model):

    # generic info
    studio_release_title = models.CharField(max_length=250, default="")
    original_language = models.CharField(max_length=10, default="", blank=True)
    country_of_origin = models.CharField(max_length=2, default="", blank=True)
    copyright_line = models.CharField(max_length=2, default="", blank=True)
    release_date = models.DateField(default=date.today, blank=True, null=True)
    production_company = models.CharField(max_length=250, default="", blank=True)

    # localization
    title_en = models.CharField(max_length=250, default="", blank=True)
    synopsis_long_en = models.CharField(max_length=1000, default="", blank=True)
    synopsis_short_en = models.CharField(max_length=250, default="", blank=True)
    title_fr = models.CharField(max_length=250, default="", blank=True)
    synopsis_long_fr = models.CharField(max_length=1000, default="", blank=True)
    synopsis_short_fr = models.CharField(max_length=250, default="", blank=True)

    # itunes info
    itunes_est_start_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_est_end_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_vod_start_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_vod_end_date = models.DateField(default=date.today, blank=True, null=True)
    itunes_sd_price_tier = models.IntegerField(default=0, blank=True)
    itunes_hd_price_tier = models.IntegerField(default=0, blank=True)

    # sasktel info
    sasktel_license_start_date = models.DateField(default=date.today, blank=True, null=True)
    sasktel_license_end_date = models.DateField(default=date.today, blank=True, null=True)
    sasktel_rating = models.CharField(max_length=10, default="NR", blank=True)
    sasktel_sd_price = models.FloatField(default=5.95)
    sasktel_hd_price = models.FloatField(default=6.95)

    # foreign key
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("metadata:metadata_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.studio_release_title


class CastCrew(models.Model):
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    apple_id = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("assetmanage:asset_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.first_name + self.last_name
