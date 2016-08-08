from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
from xml.etree import ElementTree
import xml.dom.minidom
import csv

from .models import Metadata
from projectmanage.models import Project
from assetmanage.models import Video, Audio, Subtitle


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    projects = Project.objects.all()
    return render(request, "metadata/index.html", {"time_now": time_now, "projects": projects, })


@login_required(login_url="portal/login")
def download_csv(request, pk):
    #  create the objects to process
    metadata = Metadata.objects.get(pk=pk)
    project_title = metadata.project.title
    project_source = metadata.project.pk
    videos = Video.objects.filter(project=project_source)
    audios = Audio.objects.filter(project=project_source)
    subs = Subtitle.objects.filter(project=project_source)
    meta_list = [metadata, ]

    #  convert tables to xml
    combined = list(chain(meta_list, videos, audios, subs, ))
    data = serializers.serialize("xml", combined)
    root = ElementTree.fromstring(data)

    #  create the HttpResponse object with the appropriate CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s_metadata.csv' % project_title

    writer = csv.writer(response)

    for element in root.findall(".//field"):
        writer.writerow([element.attrib["name"], element.text])

    #  send the csv for download
    return response


@login_required(login_url="portal/login")
def download_xml(request, pk):
    #  create the objects to process
    metadata = Metadata.objects.get(pk=pk)
    project_title = metadata.project.title
    project_source = metadata.project.pk
    videos = Video.objects.filter(project=project_source)
    audios = Audio.objects.filter(project=project_source)
    subs = Subtitle.objects.filter(project=project_source)
    meta_list = [metadata, ]

    #  convert tables to xml
    combined = list(chain(meta_list, videos, audios, subs, ))
    data = serializers.serialize("xml", combined)
    dom = xml.dom.minidom.parseString(data).toprettyxml()

    #  send the xml for download
    response = HttpResponse(dom, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s_metadata.csv' % project_title
    return response


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


class MetadataGeneral(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    fields = [
        "studio_release_title",
        "release_date",
        "production_company",
        "title_en",
        "synopsis_long_en",
        "synopsis_short_en",
        "title_fr",
        "synopsis_long_fr",
        "synopsis_short_fr",
    ]


class MetadataItunes(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    fields = [
        "itunes_est_start_date",
        "itunes_est_end_date",
        "itunes_vod_start_date",
        "itunes_vod_end_date",
        "itunes_sd_price_tier",
        "itunes_hd_price_tier",
    ]


class MetadataSasktel(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Metadata
    fields = [
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
