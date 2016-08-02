from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm, CommentForm


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
            post.name = request.user.get_full_name()
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
            post.name = request.user.get_full_name()
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


@login_required(login_url="portal/login")
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'news/post_draft_list.html', {'posts': posts})


@login_required(login_url="portal/login")
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('news:post_detail', pk=pk)


@login_required(login_url="portal/login")
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('news:post_list')


@login_required(login_url="portal/login")
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.name = request.user.get_full_name()
            comment.post = post
            comment.save()
            return redirect('news:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'news/add_comment.html', {'form': form})
