from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام کامل')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(verbose_name='متن پیام')
    response = models.TextField(verbose_name='پاسخ')
    is_read = models.BooleanField(verbose_name='خوانده شده', default=False)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.title