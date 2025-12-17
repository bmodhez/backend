from django.contrib import admin
from assets.models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "asset_tag",
        "category",
        "status",
        "assigned_to",
        "location",
        "purchase_cost",
        "created_at",
    )

    search_fields = ("name", "asset_tag", "serial")
    list_filter = ("status", "category", "location")
