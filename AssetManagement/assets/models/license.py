from django.db import models


class License(models.Model):
    name = models.CharField(max_length=200)

    product_key = models.CharField(max_length=255)      
    manufacturer = models.CharField(max_length=200)     

    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    licensed_to_name = models.CharField(max_length=200, blank=True, null=True)
    licensed_to_email = models.EmailField(blank=True, null=True)

    expiration_date = models.DateField()                

    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
