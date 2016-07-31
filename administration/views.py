from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    return render(request, "administration/index.html", {"time_now": time_now})


@login_required(login_url="portal/login")
def database(request):
    return render(request, "administration/database.html")


@login_required(login_url="portal/login")
def project_database_image(request):
    return render(request, "administration/project_database_image.html")


@login_required(login_url="portal/login")
def global_database_image(request):
    return render(request, "administration/global_database_image.html")
