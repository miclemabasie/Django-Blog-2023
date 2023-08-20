from bs4 import BeautifulSoup
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import PostSerializer
from django.http import JsonResponse
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity,
)
from django.utils.text import slugify
import time, logging
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token

from .models import Post
from .forms import EmailPostForm, CommentForm, SearchForm, CreatePostForm
from taggit.models import Tag


def index(request):
    posts = Post.objects.published().order_by("-created")
    template_name = "home.html"
    context = {
        "posts": posts,
    }

    return render(request, template_name, context)


def post_list(request, tag_slug=None):
    posts = Post.objects.published()
    # Check if a tag_slug was passed into the request
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        print(posts)
        posts = posts.filter(tags__in=[tag])
        print(posts)
    time.sleep(2)
    start = int(request.GET.get("start"))
    end = int(request.GET.get("end"))

    max_len = len(posts)
    if start > max_len or end > max_len:
        if start < max_len:
            posts = posts[start:max_len]
            serializer = PostSerializer(posts, many=True)
            return JsonResponse(serializer.data, safe=False)
        data = "Request out of range"
        logging.error(data)
        return JsonResponse({"message": data})

    posts = posts[start:end]

    serializer = PostSerializer(posts, many=True)
    # time.sleep(2)
    return JsonResponse(serializer.data, safe=False)


def post_detail(request, year, month, day, post):
    print("############ print from django view")
    print(post, year, month, day)
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        # publish__year=year,
        # publish__month=month,
        # publish__day=day,
    )
    print("##########33 Post", post)
    comments = post.comments.all()
    new_comment = None
    # Check for a post request for the comments
    if request.method == "POST":
        # A comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create comment object bu don't save to the database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": comments,
        "new_comment": new_comment,
    }
    template_name = "blog/post/detail.html"

    return render(request, template_name, context)


def post_share(request, post_id):
    # Retrieve the post from the database by the id
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form fields passed all validation
            cd = form.cleaned_data
            # .....Send mail
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd.get('name')} recommends you read {post.title}"
            message = f"REad {post.title} at {post_url} \n\n {cd.get('name')}'s comments: {cd.get('comments')}"
            send_mail(subject, message, "admin@mail.com", [cd.get("to")])

            sent = True

    else:
        form = EmailPostForm()

    template_name = "blog/post/share.html"
    context = {
        "post": post,
        "sent": sent,
        "form": form,
    }
    return render(request, template_name, context)


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            search_vector = SearchVector("title", weight="A") + SearchVector(
                "body", weight="B"
            )
            search_query = SearchQuery(query)

            results = (
                Post.objects.published()
                .annotate(
                    search=search_vector, rank=SearchRank(search_vector, search_query)
                )
                .filter(rank__gte=0.2)
                .order_by("-rank")
            )
            # Search using trigram similarity
            # results = (
            #     Post.objects.published()
            #     .annotate(
            #         similarity=TrigramSimilarity("title", query),
            #     )
            #     .filter(similarity__gt=0.1)
            #     .order_by("-similarity")
            # )

    template_name = "blog/post/search.html"
    context = {
        "form": form,
        "results": results,
        "query": query,
    }

    return render(request, template_name, context)


def post_upload(request):
    template_name = "blog/post/upload.html"
    context = {}
    form = CreatePostForm(request.POST or None)
    if request.method == "POST":
        post = form.save(commit=False)
        post.author = request.user
        post.slug = slugify(post.title)
        post.save()
        return redirect("/")
    else:
        context["form"] = form
    return render(request, template_name, context)


@requires_csrf_token
def uploadi(request):
    f = request.FILES["image"]
    fs = FileSystemStorage()
    filename = str(f).split(".")[0]
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    return JsonResponse({"success": 1, "file": {"url": fileurl}})


@requires_csrf_token
def uploadf(request):
    f = request.FILES["file"]
    fs = FileSystemStorage()
    filename, ext = str(f).split(".")
    print(filename, ext)
    file = fs.save(str(f), f)
    fileurl = fs.url(file)
    fileSize = fs.size(file)
    return JsonResponse(
        {"success": 1, "file": {"url": fileurl, "name": str(f), "size": fileSize}}
    )


def upload_link_view(request):
    print(request.GET["url"])
    url = request.GET["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    metas = soup.find_all("meta")
    description = ""
    title = ""
    image = ""
    for meta in metas:
        if "property" in meta.attrs:
            if meta.attrs["property"] == "og:image":
                image = meta.attrs["content"]
        elif "name" in meta.attrs:
            if meta.attrs["name"] == "description":
                description = meta.attrs["content"]
            if meta.attrs["name"] == "title":
                title = meta.attrs["content"]
    return JsonResponse(
        {
            "success": 1,
            "meta": {
                "description": description,
                "title": title,
                "image": {"url": image},
            },
        }
    )
