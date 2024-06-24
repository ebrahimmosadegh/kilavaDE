from django.db import models
from tinymce import models as tinymce_models
from django.core.validators import FileExtensionValidator
# Create your models here.

def upload_media_path(instance, filename):
    return f"about/{filename}"

class AboutUs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ پیام")
    text = tinymce_models.HTMLField(verbose_name='متن درباره ما')
    bg_aboutus = models.ImageField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='عکس کاور:', help_text="resulotion(1920*600) , acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره'
