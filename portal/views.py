from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .utils import generic_search
from assetmanage.models import Video, Audio, Subtitle, Image, Note
from projectmanage.models import Provider, Project
from metadata.models import Metadata
from news.models import Post


QUERY = "search-query"

MODEL_MAP = {
    Video: [
        "locale",
        "format",
    ],
    Provider: [
        "name",
        "itunes_code",
    ],
    Project: [
        "title",
    ],
}


@login_required(login_url="portal/login")
def search(request):
    objects = []

    for model, fields in MODEL_MAP.items():
        objects += generic_search(request, model, fields, QUERY)

    return render_to_response(
        "portal/search_results.html",
        {
            "objects": objects,
            "search_string": request.GET.get(QUERY, ""),
        }
    )


@login_required(login_url="portal/log")
def index(request):
    time_now = timezone.now()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "portal/index.html", {"time_now": time_now, "posts": posts})


def logout_user(request):
    logout(request)
    return redirect("portal:login")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect("portal:index")

            else:
                return render(request, 'portal/login.html', {'error_message': 'Your account has been disabled'})

        else:
            return render(request, 'portal/login.html', {'error_message': 'Invalid login'})

    return render(request, 'portal/login.html')
