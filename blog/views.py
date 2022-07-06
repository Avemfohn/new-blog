from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Author, Tag, Category, Post
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from .forms import FeedbackForm
from django.contrib import messages
from django.core.mail import mail_admins
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django_project import helpers


def index(request):
    return HttpResponse("Hello Django")


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id, post_slug):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post, category=category)
    paginator = Paginator(posts, 5)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        posts = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post, tags=tag)
    paginator = Paginator(posts, 5)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        posts = paginator.page(paginator.num_pages)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context)


def test_redirect(request):
    return redirect('post_list', permanent=True)


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)

        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(
                f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)

            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')

    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})
