from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag


def post_list(request, tag_slug=None):
    posts = Post.objects.published()
    # Check if a tag_slug was passed into the request
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        print(posts)
        posts = posts.filter(tags__in=[tag])
        print(posts)

    paginator = Paginator(posts, 2)
    page = request.GET.get("page")

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
        "tag": tag,
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
