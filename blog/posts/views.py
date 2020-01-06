from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Post, Category, Comment
from django.http import Http404
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.all().order_by('date')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    # post = get_object_or_404(Post, slug=slug)
    # Add comment
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:detail', slug=slug)
    else:
        form = forms.CommentForm()
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'post_detail.html', context)

@login_required(login_url="/accounts/login/")
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'create_post.html', {'form': form})

@login_required(login_url="/accounts/login/")
def post_update(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('post_list')

    post = get_object_or_404(Post, slug=slug)

    if post.author != user:
        raise Http404("you have no authority")
    else:
        if request.method == "POST":
            form = forms.CreatePost(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('posts:detail', slug=slug)
        else:
            form = forms.CreatePost(instance=post)
        return render(request, 'post_update.html', {'form': form})

@login_required(login_url="/accounts/login/")
def post_delete(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('post_list')

    post = get_object_or_404(Post, slug=slug)

    if post.author != user:
        raise Http404("you have no authority")
    else:
        post.delete()
        return redirect('posts:list')

def category_post(request, category_slug):
    category_post = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug = category_slug)
    context = {
        'category': category_post,
        'posts': posts
    }
    return render(request, 'category_post_list.html', context)

# @login_required(login_url="/accounts/login/")
# def add_comment_to_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     if request.method == "POST":
#         form = forms.CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             return redirect('posts:detail', slug=slug)
#     else:
#         form = forms.CommentForm()
#     return render(request, 'add_comment_to_post.html', {'form': form})

@login_required(login_url="/accounts/login/")
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('posts:detail', slug=comment.post.slug)
