from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.forms import PostForm
from django.contrib import messages
from blog.models import Post, Author, Category, Tag


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
