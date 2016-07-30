from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.uploadhandler import TemporaryFileUploadHandler

from .forms import AssetForm, VideoForm, AudioForm, SubtitleForm, ImageForm, NoteForm
from .models import Asset, Video, Audio, Subtitle, Image, Note


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    return render(request, "assetmanage/index.html", {"time_now": time_now})


@login_required(login_url="portal/login")
def search(request):
    return render(request, 'assetmanage/search.html')


@login_required(login_url="portal/login")
def asset_select(request):
    return render(request, 'assetmanage/asset_select.html')


# @login_required(login_url="portal/login")
# def asset_select(request):
#     if request.method == 'POST':
#         print("1")
#         fichier = request.FILES["asset_file"]
#         print(fichier)
#         print(fichier.name)
#
#         form = AssetTestForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             print("2")
#             form.save(commit=False)
#             temp_file_obj = TemporaryFileUploadHandler(form.cleaned_data['file_path'])
#             form.instance.file_size = temp_file_obj.chunk_size
#             form.instance.file_name = form.cleaned_data['file_path'].split("/")[-1]
#             form.save()
#             return HttpResponseRedirect('/assetmanage/assets/')
#
#         print(form.errors)
#
#     else:
#         print("4")
#         form = AssetTestForm()
#
#     return render(request, 'assetmanage/asset_select.html', {'form': form})


#  https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/
def add_video(request):
    if request.method == "POST":
        aform = AssetForm(request.POST, instance=Asset())
        bform = VideoForm(request.POST, instance=Video())

        if aform.is_valid() and bform.is_valid():
            new_asset = aform.save()
            new_video = bform.save(commit=False)
            new_video.asset = new_asset
            new_video.save()
            return HttpResponseRedirect('/video/add/')
    else:
        aform = AssetForm(instance=Asset())
        bform = VideoForm(instance=Video())
    return render_to_response('assetmanage/video_add.html', {'asset_form': aform, 'video_form': bform})


class AssetsView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "assetmanage/assets.html"
    context_object_name = "assets_list"

    def get_queryset(self):
        return Asset.objects.all()


class AssetDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    template_name = "assetmanage/asset_details.html"


class AssetCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    fields = ["file_name", "file_path", "type", "file_size", "file_md5", "project", "provider", "status"]


class AssetUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    fields = ["file_name", "file_path", "type", "file_size", "file_md5", "project", "provider", "status"]


class AssetDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    success_url = reverse_lazy("assetmanage:assets")
