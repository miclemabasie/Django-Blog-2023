from .models import Post, Category


def recent_posts(request):
    posts = Post.objects.order_by("-created")[
        :5
    ]  # get 5 most recent posts by date created
    context = {"recent_posts": posts}
    return context


def categories(reqeust):
    categories = Category.objects.all()
    context = {"categories": categories}
    return context
