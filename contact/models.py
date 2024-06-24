from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class ContactUs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ پیام")
    fullname = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    call = models.CharField(max_length=50, verbose_name='شماره تماس')
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام')
    text = tinymce_models.HTMLField(verbose_name='متن پیام')
    is_read = models.BooleanField(verbose_name='خوانده شده / نشده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'

    def __str__(self):
        return self.subject
