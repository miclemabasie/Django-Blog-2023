from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    posts = Post.objects.published()
    paginator = Paginator(posts, 2)
    page = request.GET.get("page")
    print("##################33", page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page isnot an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is oput of range deliver last page of results
        posts = paginator.page(paninator.num_pages)

    template_name = "blog/post/list.html"
    context = {
        "page": page,
        "post_list": posts,
    }
    return render(request, template_name, context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    context = {
        "post": post,
    }
    template_name = "blog/post/detail.html"

    return render(request, template_name, context)
