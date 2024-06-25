from django.db import models
from tinymce import models as tinymce_models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
# Create your models here.

def upload_media_path(instance, filename):
    return f"about/{filename}"

class AboutUs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="date:")
    text = tinymce_models.HTMLField(verbose_name='text about us:')
    bg_aboutus = models.ImageField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='cover image:', help_text="resulotion(1920*600) , acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us Kilava'

@receiver(pre_save, sender=AboutUs)
def delete_old_image_category(sender, instance, *args, **kwargs):
        if instance.pk:
            g_file = AboutUs.objects.get(pk=instance.pk)

            if instance.bg_aboutus and g_file.bg_aboutus != instance.bg_aboutus:
                g_file.bg_aboutus.delete(False)

@receiver(pre_delete, sender=AboutUs)
def service_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.bg_aboutus.delete(False)