from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Provider, Project


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    return render(request, "projectmanage/index.html", {"time_now": time_now})


@login_required(login_url="portal/login")
def search(request):
    return render(request, 'projectmanage/search.html')


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
    fields = ["title", "itunes", "google", "sasktel", "netflix", "status", "provider"]


class ProviderUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Provider
    fields = ["name", "itunes_code", "itc_user", "itc_password"]


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    fields = ["title", "itunes", "google", "sasktel", "netflix", "status", "provider"]


class ProviderDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Provider
    success_url = reverse_lazy("portal:providers")


class ProjectDelete(LoginRequiredMixin, DeleteView):
    login_url = '/portal/login/'
    redirect_field_name = 'redirect_to'
    model = Project
    success_url = reverse_lazy("portal:projects")
