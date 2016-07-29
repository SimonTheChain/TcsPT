from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.uploadhandler import TemporaryFileUploadHandler

from .forms import AssetForm, AssetTestForm
from .models import Asset, AssetTest, ImageAsset


@login_required(login_url="portal/login")
def index(request):
    mtl_now = timezone.now()
    return render(request, "assetmanage/index.html", {"mtl_time": mtl_now})


@login_required(login_url="portal/login")
def search(request):
    return render(request, 'assetmanage/search.html')


# @login_required(login_url="portal/login")
# def asset_select(request):
#     form = AssetSelectForm
#
#     if request.method == "POST":
#         form = AssetSelectForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             asset = form.save(commit=False)
#             asset.file_path = request.file_path
#     return render(request, {"form": form})


@login_required(login_url="portal/login")
def asset_create(request):
    return render(request, 'assetmanage/asset_create.html')


@login_required(login_url="portal/login")
def asset_select(request):
    if request.method == 'POST':
        print("1")
        fichier = request.FILES["asset_file"]
        print(fichier)
        print(fichier.name)

        form = AssetTestForm(request.POST, request.FILES)

        if form.is_valid():
            print("2")
            form.save(commit=False)
            temp_file_obj = TemporaryFileUploadHandler(form.cleaned_data['file_path'])
            form.instance.file_size = temp_file_obj.chunk_size
            form.instance.file_name = form.cleaned_data['file_path'].split("/")[-1]
            form.save()
            return HttpResponseRedirect('/assetmanage/assets/')

        print(form.errors)

    else:
        print("4")
        form = AssetTestForm()

    return render(request, 'assetmanage/asset_select.html', {'form': form})
    #  return render(request, 'assetmanage/asset_select.html')


# @login_required(login_url="portal/login")
# def asset_test(request):
#     path = request.POST["asset_select"]
#     return render(request, 'assetmanage/asset_test.html', {"path": path})


@login_required(login_url="portal/login")
def asset_test(request):
    if request.method == 'POST':
        print("1")
        form = AssetTestForm(request.POST)

        if form.is_valid():
            print("2")
            form.save(commit=False)
            temp_file_obj = TemporaryFileUploadHandler(form.cleaned_data["file_path"])
            form.file_size = temp_file_obj.chunk_size
            form.save()
            return HttpResponseRedirect('/assetmanage/assets/')

        print("3")

    else:
        print("4")
        form = AssetTestForm()

    return render(request, 'assetmanage/asset_select.html', {'form': form})


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


@login_required(login_url="portal/login")
def add_asset(request):
    form = AssetForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }
    return render(request, "assetmanage/asset_form.html", context)


class AssetCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    fields = ["fichier", "provider", "project", "type", "file_md5", "status"]


class AssetUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    fields = ["provider", "project", "fichier", "type", "file_md5", "status"]


class AssetDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Asset
    success_url = reverse_lazy("assetmanage:assets")


class ImagesView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "assetmanage/images.html"
    context_object_name = "images_list"

    def get_queryset(self):
        return ImageAsset.objects.all()


class ImageDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = ImageAsset
    template_name = "assetmanage/image_details.html"


class ImageCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = ImageAsset
    fields = ["provider", "project", "thumbnail", "itunes", "sasktel"]


class ImageUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = ImageAsset
    fields = ["provider", "project", "thumbnail", "itunes", "sasktel"]


class ImageDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = ImageAsset
    success_url = reverse_lazy("assetmanage:images")
