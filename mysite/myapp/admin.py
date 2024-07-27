from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "views_count", "position")
    list_filter = ("position",)
    search_fields = ("title",)
    ordering = ("position",)
