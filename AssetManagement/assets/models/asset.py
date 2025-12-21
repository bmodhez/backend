from django.db import models
from django.conf import settings


class Asset(models.Model):

    STATUS_READY = "ready"
    STATUS_DEPLOYED = "deployed"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = [
        (STATUS_READY, "Ready"),
        (STATUS_DEPLOYED, "Deployed"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    asset_tag = models.CharField(max_length=100, unique=True)
    serial = models.CharField(max_length=150, blank=True)

    category = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_READY
    )

    is_deleted = models.BooleanField(default=False)

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_assets"
    )

    location = models.CharField(max_length=150, blank=True)

    purchase_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="assets/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.asset_tag})"