from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    slug = models.SlugField(max_length=250, unique_for_date="created")
    description = models.TextField()
    image = models.ImageField(upload_to="media/categories")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"


class PublishedManager(models.Manager):
    def published(self):
        qs = super(PublishedManager, self).get_queryset().filter(status="published")
        return qs


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(
        Category,
        related_name="posts",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="media/%Y_%m_%d", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
    )
    tags = TaggableManager()
    objects = PublishedManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )

    def get_intro(self):
        text = self.body.split(" ")[0:30]
        content = " ".join(text)
        return content


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",  # allows us to use (Post.comments.all()) -> comment_set by default
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
