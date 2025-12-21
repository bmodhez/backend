from django.contrib import admin
from assets.models import Asset, License, Accessory, Consumable, Component


class SoftDeleteAdmin(admin.ModelAdmin):


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    # single delete
    def delete_model(self, request, obj):
        obj.is_deleted = True
        obj.save()

    # bulk delete
    def delete_queryset(self, request, queryset):
        queryset.update(is_deleted=True)



@admin.register(Asset)
class AssetAdmin(SoftDeleteAdmin):
    list_display = (
        "name",
        "asset_tag",
        "category",
        "status",
        "assigned_to",
        "location",
        "created_at",
    )
    list_filter = ("status", "category", "location")
    search_fields = ("name", "asset_tag", "serial")
    ordering = ("-created_at",)


@admin.register(License)
class LicenseAdmin(SoftDeleteAdmin):
    list_display = (
        "name",
        "manufacturer",
        "total_seats",
        "available_seats",
        "expiration_date",
        "created_at",
    )
    list_filter = ("manufacturer", "expiration_date")
    search_fields = ("name", "product_key")
    ordering = ("expiration_date",)


@admin.register(Accessory)
class AccessoryAdmin(SoftDeleteAdmin):
    list_display = ("name", "category", "quantity", "location", "created_at")
    list_filter = ("category", "location")
    search_fields = ("name",)


@admin.register(Consumable)
class ConsumableAdmin(SoftDeleteAdmin):
    list_display = ("name", "category", "quantity", "location", "created_at")
    list_filter = ("category", "location")
    search_fields = ("name",)


@admin.register(Component)
class ComponentAdmin(SoftDeleteAdmin):
    list_display = ("name", "category", "quantity", "location", "created_at")
    list_filter = ("category", "location")
    search_fields = ("name",)
