from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers
from django.http import HttpResponse
import xml.dom.minidom
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
    dom = xml.dom.minidom.parseString(data).toprettyxml()
    filename = os.path.splitext(Video.objects.get(pk=pk).file_name)[0]
    response = HttpResponse(dom, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s.xml' % filename
    return response


@login_required(login_url="portal/login")
def download_audio_xml(request, pk):
    data = serializers.serialize("xml", [Audio.objects.get(pk=pk), ])
    dom = xml.dom.minidom.parseString(data).toprettyxml()
    filename = os.path.splitext(Audio.objects.get(pk=pk).file_name)[0]
    response = HttpResponse(dom, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s.xml' % filename
    return response


@login_required(login_url="portal/login")
def download_subtitle_xml(request, pk):
    data = serializers.serialize("xml", [Subtitle.objects.get(pk=pk), ])
    dom = xml.dom.minidom.parseString(data).toprettyxml()
    filename = os.path.splitext(Subtitle.objects.get(pk=pk).file_name)[0]
    response = HttpResponse(dom, content_type='text/xml')
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


class AudiosView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "assetmanage/audios.html"
    context_object_name = "audios_list"

    def get_queryset(self):
        return Audio.objects.all()


class AudioDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Audio
    template_name = "assetmanage/audio_details.html"


class AudioCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Audio
    fields = [
        "project",
        "type",
        "file_name",
        "file_path",
        "file_size",
        "file_md5",
        "locale",
        "channel_1",
        "channel_2",
        "channel_3",
        "channel_4",
        "channel_5",
        "channel_6",
        "channel_7",
        "channel_8",
        "status",
    ]


class AudioUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Audio
    fields = [
        "project",
        "type",
        "file_name",
        "file_path",
        "file_size",
        "file_md5",
        "locale",
        "channel_1",
        "channel_2",
        "channel_3",
        "channel_4",
        "channel_5",
        "channel_6",
        "channel_7",
        "channel_8",
        "status",
    ]


class AudioDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Audio
    success_url = reverse_lazy("assetmanage:audios")


class SubtitlesView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "assetmanage/subtitles.html"
    context_object_name = "subtitles_list"

    def get_queryset(self):
        return Subtitle.objects.all()


class SubtitleDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Subtitle
    template_name = "assetmanage/subtitle_details.html"


class SubtitleCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Subtitle
    fields = [
        "project",
        "type",
        "file_name",
        "file_path",
        "file_size",
        "file_md5",
        "locale",
        "status",
    ]


class SubtitleUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Subtitle
    fields = [
        "project",
        "type",
        "file_name",
        "file_path",
        "file_size",
        "file_md5",
        "locale",
        "status",
    ]


class SubtitleDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Subtitle
    success_url = reverse_lazy("assetmanage:subtitles")
