from django.db import models

class Asset(models.Model):
    print(models)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="assets/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
