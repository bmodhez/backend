from django.db import models
from django.conf import settings


class Asset(models.Model):

    STATUS_CHOICES = [
        ("ready", "Ready"),
        ("deployed", "Deployed"),
        ("repair", "Repair"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    asset_tag = models.CharField(max_length=100, unique=True)
    serial = models.CharField(max_length=150, blank=True)

    category = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ready"
    )

    assigned_to = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)

    location = models.CharField(max_length=150, blank=True)

    purchase_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    image = models.ImageField(upload_to="assets/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.asset_tag})"
