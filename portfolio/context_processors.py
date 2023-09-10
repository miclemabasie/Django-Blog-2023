from .models import Portfolio


def recent_works(request):
    works = Portfolio.objects.order_by("-created")[
        :5
    ]  # get 5 most recent works by date created
    context = {"recent_works": works}
    return context
