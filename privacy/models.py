from django.db import models
from tinymce import models as tinymce_models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
# Create your models here.

def upload_media_path(instance, filename):
    return f"privacy/{filename}"

class Datenschutz(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="date:")
    text = tinymce_models.HTMLField(verbose_name='content datenschutz:')
    bg_datenschutz = models.ImageField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='cover image:', help_text="resulotion(1920*600) , acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')

    class Meta:
        verbose_name = 'Datenschutz'
        verbose_name_plural = 'Datenschutz website'

@receiver(pre_save, sender=Datenschutz)
def delete_old_image_category(sender, instance, *args, **kwargs):
        if instance.pk:
            g_file = Datenschutz.objects.get(pk=instance.pk)

            if instance.bg_datenschutz and g_file.bg_datenschutz != instance.bg_datenschutz:
                g_file.bg_datenschutz.delete(False)

@receiver(pre_delete, sender=Datenschutz)
def service_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.bg_datenschutz.delete(False)


class Impressum(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="date:")
    text = tinymce_models.HTMLField(verbose_name='content impressum:')
    bg_impressum = models.ImageField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='cover image:', help_text="resulotion(1920*600) , acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')

    class Meta:
        verbose_name = 'Impressum'
        verbose_name_plural = 'Impressum website'

@receiver(pre_save, sender=Impressum)
def delete_old_image_category(sender, instance, *args, **kwargs):
        if instance.pk:
            g_file = Impressum.objects.get(pk=instance.pk)

            if instance.bg_impressum and g_file.bg_impressum != instance.bg_impressum:
                g_file.bg_impressum.delete(False)

@receiver(pre_delete, sender=Impressum)
def service_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.bg_impressum.delete(False)