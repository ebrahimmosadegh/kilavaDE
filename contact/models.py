from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class ContactUs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="date:")
    fullname = models.CharField(max_length=200, verbose_name='name and family:')
    email = models.EmailField(max_length=100, verbose_name='email:')
    call = models.CharField(max_length=50, verbose_name='call number')
    subject = models.CharField(max_length=200, verbose_name='subject')
    text = tinymce_models.HTMLField(verbose_name='text:')
    is_read = models.BooleanField(verbose_name='readed:')

    class Meta:
        verbose_name = 'contact us'
        verbose_name_plural = 'contact users'

    def __str__(self):
        return self.subject
