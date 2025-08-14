from django.utils.text import slugify
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import SlugField


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name="Subtitle",db_index=True)
    url_title = models.CharField(max_length=120, verbose_name="URL Subtitle",db_index=True)
    is_active = models.BooleanField(default=True, verbose_name="Is active?")
    is_deleted = models.BooleanField(default=False, verbose_name="Is deleted?")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.title}, {self.url_title}'

class Product(models.Model):
    title = models.CharField(max_length=300,verbose_name="Subtitle",db_index=True)
    category = models.ManyToManyField(ProductCategory, verbose_name='Categories',related_name='product_categories')
    price = models.IntegerField(verbose_name='Price')
    rating = models.IntegerField(null=True, validators = [MinValueValidator(0), MaxValueValidator(5)])
    is_active = models.BooleanField(verbose_name='Is Active',null=True,default=True)
    short_description = models.CharField(null=True, max_length=300,db_index=True,verbose_name="Short Description")
    description = models.TextField(null=True, blank=True, verbose_name="Description",db_index=True)
    slug = SlugField(default="", null=False,blank=True,db_index=True,unique=True,verbose_name="Url Subtitle")
    is_deleted = models.BooleanField(default=False,verbose_name='Is deleted?')

    def __str__(self):
        return f"{self.title}, {self.price}$"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class ProductTag(models.Model):
    caption = models.CharField(max_length=120,verbose_name='Tag',db_index=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='ProductTags')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.caption
