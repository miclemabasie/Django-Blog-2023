from django.contrib import admin
from .models import Post, Comment, Category, Common


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "publish",
        "status",
    )

    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = (
        "author",
    )  # Allows the ability to search user when making an entry
    date_hierarchy = "publish"
    ordering = ("status", "publish")  # For sorting the tables


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentADmin(admin.ModelAdmin):
    list_display = ("name", "email", "post", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("name", "email", "body")
    raw_id_fields = ("post",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created", "updated"]
    search_fields = ("name", "created")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Common)
class CommonAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]
