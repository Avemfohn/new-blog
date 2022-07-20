from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.forms import PostForm
from django.contrib import messages
from blog.models import Post, Author, Category, Tag
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def post_add(request):
    if request.method == "POST":
        f = PostForm(request.POST)

        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Post added.')
            return redirect('post_add')
    else:
        f = PostForm()
    return render(request, 'cadmin/post_add.html', {'form': f})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        f = PostForm(request.POST, instance=post)

        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Post updated.')
            return redirect(reverse('post_update', args=[post.id]))
    else:
        f = PostForm(instance=post)

    return render(request, 'cadmin/post_update.html', {'form': f, 'post': post})


@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'cadmin/admin_page.html')


def login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('/cadmin/')
    else:
        return auth_views.login(request, **kwargs)


def password_change_done(request):
    if request.user.is_authenticated:
        return render(request, 'cadmin\password_change_done.html')


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'cadmin/register.html', {'form': f})
