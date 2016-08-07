from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


PROJECT_STATUS = (
        ("preprod", "In Pre-Production"),
        ("completed", "Completed"),
        ("Prequal", (
            ("prequalready", "Ready for Prequal"),
            ("prequalprogress", "Prequal in progress"),
            ("prequaldone", "Prequal Done"),
        )
         ),
        ("Qc", (
            ("qcready", "Ready for Qc"),
            ("qcprogress", "Qc in progress"),
            ("qcdone", "Qc Done"),
        )
         ),
        ("Packaging", (
            ("packready", "Ready for Packaging"),
            ("packprogress", "Packaging in progress"),
            ("packdone", "Packaging Done"),
        )
         ),
        ("Metadata", (
            ("metaready", "Ready for Metadata"),
            ("metaprogress", "Metadata in progress"),
            ("metadone", "Metadata Done"),
        )
         ),
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
    )


PLATFORMS = (
    ("itunes", "iTunes"),
    ("google", "Google"),
    ("sasktel", "Sasktel"),
    ("netflix", "Netflix"),
)


REJECTION_STATUS = (
    ("open", "Issue open"),
    ("closed", "Issue resolved"),
)


class Provider(models.Model):
    name = models.CharField(max_length=250, default="")
    itunes_code = models.CharField(max_length=250, default="", blank=True, null=True)
    itc_user = models.CharField(max_length=250, default="", blank=True, null=True)
    itc_password = models.CharField(max_length=250, default="", blank=True, null=True)

    def get_absolute_url(self):
        return reverse("projectmanage:provider_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250, default="")
    platform = models.CharField(max_length=250, choices=PLATFORMS, default="itunes")
    start_date = models.DateField(default=date.today)
    due_date = models.DateField(default=date.today, blank=True, null=True)
    status = models.CharField(max_length=25, choices=PROJECT_STATUS, default="prequalready")
    operator = models.ForeignKey(User, blank=True, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("projectmanage:project_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Rejection(models.Model):
    reason = models.CharField(max_length=1000, default="")
    details = models.TextField(default="")
    action = models.CharField(max_length=1000, default="", blank=True, null=True)
    status = models.CharField(max_length=25, choices=REJECTION_STATUS, default="open")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("projectmanage:rejection_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.project.title
