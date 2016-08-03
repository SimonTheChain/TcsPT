from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers
from django.http import HttpResponse
import os

from .models import Video, Audio, Subtitle, Image, Note


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    return render(request, "assetmanage/index.html", {"time_now": time_now})


@login_required(login_url="portal/login")
def asset_select(request):
    return render(request, 'assetmanage/asset_select.html')


@login_required(login_url="portal/login")
def download_video_xml(request, pk):
    data = serializers.serialize("xml", [Video.objects.get(pk=pk), ])
    filename = os.path.splitext(Video.objects.get(pk=pk).file_name)[0]
    response = HttpResponse(data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s.xml' % filename
    return response


class VideosView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "assetmanage/videos.html"
    context_object_name = "videos_list"

    def get_queryset(self):
        return Video.objects.all()


class VideoDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Video
    template_name = "assetmanage/video_details.html"


class VideoCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
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


class VideoUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
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


class VideoDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Video
    success_url = reverse_lazy("assetmanage:videos")
