from django.urls import path
from .feeds import LatestPostFeed
from . import views
from .views import uploadf, uploadi
from django.views.decorators.csrf import csrf_exempt

app_name = "blog"

urlpatterns = [
    path("<int:page>/", views.post_list, name="post_list"),
    path(
        "<int:page>/tag/<slug:tag_slug>/",
        views.post_list,
        name="post_list_by_tag",
    ),
    path(
        "<int:page>/category/<slug:category>/",
        views.post_list,
        name="post_list_by_category",
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path(
        "<int:post_id>/share/",
        views.post_share,
        name="post_share",
    ),
    path("feed/", LatestPostFeed(), name="post_feed"),
    path("search/", views.post_search, name="post_search"),
    path("create-post/", views.post_upload, name="upload_post"),
    path("uploadi/", csrf_exempt(uploadi)),
    path("uploadf/", csrf_exempt(uploadf)),
    path("linkfetching/", views.upload_link_view),
]
