from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import pytz


@login_required(login_url="portal/login")
def index(request):
    time_now = timezone.now()
    return render(request, "portal/index.html", {"time_now": time_now})


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
