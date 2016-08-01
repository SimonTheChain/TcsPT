from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm


@login_required(login_url="portal/login")
def post_list(request):
    time_now = timezone.now()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news/post_list.html', {'posts': posts, "time_now": time_now})


@login_required(login_url="portal/login")
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})


@login_required(login_url="portal/login")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.name = request.user.first_name + " " + request.user.last_name
            post.published_date = timezone.now()
            post.save()
            return redirect('news:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/post_edit.html', {'form': form})


@login_required(login_url="portal/login")
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_edit.html', {'form': form})


@login_required(login_url="portal/login")
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('news:post_list')
