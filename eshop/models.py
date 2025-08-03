from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField(max_length=10)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


    def __str__(self):
        return f"{self.title}, {self.price}s"