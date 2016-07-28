from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import AssetForm, AssetTestForm
from .models import Asset, AssetTest


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
    return render(request, 'assetmanage/asset_select.html')


# @login_required(login_url="portal/login")
# def asset_test(request):
#     path = request.POST["asset_select"]
#     return render(request, 'assetmanage/asset_test.html', {"path": path})


@login_required(login_url="portal/login")
def asset_test(request):
    if request.method == 'POST':
        form = AssetTestForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/assetmanage/assets/')

    # if a GET (or any other method) we'll create a blank form
    else:
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
