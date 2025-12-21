from django.db import models

class Consumable(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    model_no = models.CharField(max_length=100, blank=True)
    item_no = models.CharField(max_length=100, blank=True)
    order_number = models.CharField(max_length=100, blank=True)

    purchase_date = models.DateField(null=True, blank=True)

    min_quantity = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()   # TOTAL
    unit_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    location = models.CharField(max_length=150)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
