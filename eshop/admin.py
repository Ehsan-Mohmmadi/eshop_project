from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    #readonly_fields = ['slug']
    prepopulated_fields = { "slug": ["title"]}
    list_display = ('title', 'price', 'rating' ,'is_active')
    list_filter = ('is_active', 'rating')
    list_editable = ['rating', 'is_active']

admin.site.register(models.Product,ProductAdmin)