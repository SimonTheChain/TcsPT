from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Metadata
from projectmanage.models import Project


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    projects = Project.objects.all()
    return render(request, "metadata/index.html", {"time_now": time_now, "projects": projects})


class MetadatasView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "metadata/metadatas.html"
    context_object_name = "metadatas_list"

    def get_queryset(self):
        return Metadata.objects.all()


class MetadataDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    template_name = "metadata/metadata_details.html"


class MetadataCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    fields = [
        "project",
        "studio_release_title",
        "release_date",
        "production_company",
        "title_en",
        "synopsis_long_en",
        "synopsis_short_en",
        "title_fr",
        "synopsis_long_fr",
        "synopsis_short_fr",
        "itunes_est_start_date",
        "itunes_est_end_date",
        "itunes_vod_start_date",
        "itunes_vod_end_date",
        "itunes_sd_price_tier",
        "itunes_hd_price_tier",
        "sasktel_license_start_date",
        "sasktel_license_end_date",
        "sasktel_rating",
        "sasktel_sd_price",
        "sasktel_hd_price",
    ]


class MetadataUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    fields = [
        "project",
        "studio_release_title",
        "release_date",
        "production_company",
        "title_en",
        "synopsis_long_en",
        "synopsis_short_en",
        "title_fr",
        "synopsis_long_fr",
        "synopsis_short_fr",
        "itunes_est_start_date",
        "itunes_est_end_date",
        "itunes_vod_start_date",
        "itunes_vod_end_date",
        "itunes_sd_price_tier",
        "itunes_hd_price_tier",
        "sasktel_license_start_date",
        "sasktel_license_end_date",
        "sasktel_rating",
        "sasktel_sd_price",
        "sasktel_hd_price",
    ]


class MetadataDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    success_url = reverse_lazy("metadata:metadatas")
