from django.db import models
from django.utils.translation import gettext_lazy as _


class Portfolio(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Project Name"))
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name=_("Projects's description"))
    link = models.CharField(
        max_length=256, verbose_name=_("Link to Project"), null=True, blank=True
    )
    github = models.CharField(
        max_length=256, verbose_name=("Github Link"), null=True, blank=True
    )  # To be changed
    image1 = models.ImageField(upload_to="media/porfolio/%Y_%m_%d")
    image2 = models.ImageField(
        upload_to="media/porfolio/%Y_%m_%d", null=True, blank=True
    )
    image3 = models.ImageField(
        upload_to="media/porfolio/%Y_%m_%d", null=True, blank=True
    )
    image4 = models.ImageField(
        upload_to="media/porfolio/%Y_%m_%d", null=True, blank=True
    )
    stack = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Dated Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Date Updated"))
    is_online = models.BooleanField(default=False, verbose_name=_("Is Project Online"))

    def __str__(self):
        return f"{self.name}"

    def get_stack(self):
        """
        Return a list of elements for the tech stack
        """
        if self.stack:
            stack = self.stack.split(",")
            stack = [x for x in stack if len(x) > 0]
            return stack
        return ["Python"]
