from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.title}, {self.price}s"