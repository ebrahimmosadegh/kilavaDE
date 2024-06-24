from django.db import models
from tinymce import models as tinymce_models
from django.utils.text import slugify
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.html import format_html
from django.urls import reverse
from tools.views import unique_slug_generator
from tools.views import validate_image_extension

# Create your models here.

def upload_image_path(instance, filename):
    return f"services/{instance.id}/{filename}"

def upload_image_gallery_path(instance, filename):
    return f"services/{instance.service_id}/{filename}"

class Services(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ:")
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="عنوان:")
    subtitle = models.CharField(max_length=250, null=False, blank=False, verbose_name="توضیح مختصر:")
    image = models.ImageField(upload_to=upload_image_path, null=False, blank=False, validators=[validate_image_extension], verbose_name="عکس اصلی:", help_text="resulotion(1150*1035)")
    content = tinymce_models.HTMLField(null=False, blank=False,verbose_name='محتوا:')
    cover = models.ImageField(upload_to=upload_image_path, blank=True, null=True, validators=[validate_image_extension], verbose_name="عکس کاور:", help_text="resulotion(1920*600)")
    slug = models.SlugField(blank=False,null=False, unique=True, db_index=True, help_text="url website")

    def get_absolute_url(self):
        return reverse("Services:service", args=[self.slug])
    
    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات ها'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(Services, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super(Services, self).save(*args, **kwargs)
    
    def image_tag(self):
        return format_html("<img src='{}' width=150>".format(self.image.url))
    image_tag.short_description = 'cover image'

@receiver(pre_save, sender=Services)
def delete_old_file_service(sender, instance, *args, **kwargs):
    # if not instance.slug:
    #     instance.slug = unique_slug_generator(instance)
        
    if instance.pk:
        g_image = Services.objects.get(pk=instance.pk)
        g_cover = Services.objects.get(pk=instance.pk)
        if instance.image and g_image.image != instance.image:
            g_image.image.delete(False)

        if instance.cover and g_cover.cover != instance.cover:
            g_cover.cover.delete(False)

@receiver(pre_delete, sender=Services)
def service_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
    instance.cover.delete(False)


class Gallery(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ:")
    image = models.ImageField(upload_to=upload_image_gallery_path, null=True, blank=True, validators=[validate_image_extension], verbose_name="عکس اسلایدر:", help_text="resulotion(1200*600)")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='service:')

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری اسلایدر'
    

@receiver(pre_save, sender=Gallery)
def delete_old_gallery(sender, instance, *args, **kwargs):
    if instance.pk:
            exi_image = Gallery.objects.get(pk=instance.pk)
            if instance.image and exi_image.image != instance.image:
                exi_image.image.delete(False)

@receiver(pre_delete, sender=Gallery)
def Gallery_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)