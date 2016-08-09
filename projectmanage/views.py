from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers
from django.http import HttpResponse

from .models import Provider, Project, Rejection
from assetmanage.models import Video, Audio, Subtitle


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    projects = Project.objects.all().order_by("title")
    return render(request, "projectmanage/index.html", {"time_now": time_now, "projects": projects})


@login_required(login_url="portal/login")
def index_providers(request):
    time_now = timezone.now()
    providers = Provider.objects.all().order_by("name")
    return render(request, "projectmanage/index_providers.html", {"time_now": time_now, "providers": providers})


@login_required(login_url="portal/login")
def index_rejections(request):
    time_now = timezone.now()
    rejections = Rejection.objects.all().order_by("project")
    return render(request, "projectmanage/index_rejections.html", {"time_now": time_now, "rejections": rejections})


@login_required(login_url="portal/login")
def search(request):
    return render(request, 'projectmanage/search.html')


@login_required(login_url="portal/login")
def download_video_xml(request, pk):
    project = Project.objects.get(pk=pk)
    data = serializers.serialize("xml", [Video(project_id=pk), ])
    filename = project.title.replace(' ', '').lower()
    response = HttpResponse(data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s_video.xml' % filename
    return response


@login_required(login_url="portal/login")
def download_audio_xml(request, pk):
    project = Project.objects.get(pk=pk)
    data = serializers.serialize("xml", [Audio(project_id=pk), ])
    filename = project.title.replace(' ', '').lower()
    response = HttpResponse(data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s_audio.xml' % filename
    return response


@login_required(login_url="portal/login")
def download_subtitle_xml(request, pk):
    project = Project.objects.get(pk=pk)
    data = serializers.serialize("xml", [Subtitle(project_id=pk), ])
    filename = project.title.replace(' ', '').lower()
    response = HttpResponse(data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s_subtitle.xml' % filename
    return response


class ProvidersView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "projectmanage/providers.html"
    context_object_name = "providers_list"

    def get_queryset(self):
        return Provider.objects.all()


class ProjectsView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "projectmanage/projects.html"
    context_object_name = "projects_list"

    def get_queryset(self):
        return Project.objects.all()


class ProviderDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Provider
    template_name = "projectmanage/provider_details.html"


class ProjectDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    template_name = "projectmanage/project_details.html"


class ProviderCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Provider
    fields = ["name", "itunes_code", "itc_user", "itc_password"]


class ProjectCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    fields = ["title", "platform", "start_date", "due_date", "status", "provider", "operator", ]


class ProviderUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Provider
    fields = ["name", "itunes_code", "itc_user", "itc_password"]


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    fields = ["title", "platform", "start_date", "due_date", "status", "provider", "operator", ]


class ProjectOperator(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    fields = ["operator", ]


class ProjectStatus(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    fields = ["status", ]


class ProviderDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Provider
    success_url = reverse_lazy("projectmanage:providers")


class ProjectDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    success_url = reverse_lazy("projectmanage:projects")


class RejectionsView(LoginRequiredMixin, generic.ListView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    template_name = "projectmanage/rejections.html"
    context_object_name = "rejections_list"

    def get_queryset(self):
        return Rejection.objects.all()


class RejectionDetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Rejection
    template_name = "projectmanage/rejection_details.html"


class RejectionCreate(LoginRequiredMixin, CreateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Rejection
    fields = ["project", "reason", "details", "action", "status"]


class RejectionUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Rejection
    fields = ["project", "reason", "details", "action", "status"]


class RejectionDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Rejection
    success_url = reverse_lazy("projectmanage:rejections")
