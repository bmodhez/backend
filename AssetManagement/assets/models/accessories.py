
from django.db import models

class Accessory(models.Model):
    device_image = models.ImageField(upload_to="accessories/", blank=True, null=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=150)
    min_quantity = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
