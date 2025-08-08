from wsgiref.validate import validator
from django.utils.text import slugify

from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import SlugField


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(null=True, validators = [MinValueValidator(0), MaxValueValidator(5)])
    is_active = models.BooleanField(null=True)
    short_description = models.CharField(null=True, max_length=300)
    slug = SlugField(default="", null=False,blank=True)

    def __str__(self):
        return f"{self.title}, {self.price}$"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)