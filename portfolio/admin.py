from django.contrib import admin
from portfolio.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "github", "link", "is_online")
    list_filter = ("is_online",)
    prepopulated_fields = {"slug": ("name",)}
