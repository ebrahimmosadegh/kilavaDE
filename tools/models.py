from django.db import models
from .views import validate_image_extension
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from tinymce import models as tinymce_models
# Create your models here.

def upload_media_path(instance, filename):
    return f"Settings/{filename}"

class SettingsSite(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='عنوان وبسایت:')
    logo = models.ImageField(upload_to=upload_media_path, validators=[validate_image_extension], verbose_name='لوگو:', help_text="resulotion(120*120)")
    link = models.URLField(blank=True, verbose_name='لینک وبسایت:')
    call = models.CharField(max_length=20, blank=True, verbose_name='شماره تماس:')
    mobile = models.CharField(max_length=20, blank=True, verbose_name='شماره موبایل:')
    email = models.CharField(max_length=150, blank=True, verbose_name='ایمیل:')
    address = models.CharField(max_length=200, blank=True, verbose_name='آدرس:')
    location_maps = models.CharField(max_length=600,blank=True, verbose_name='لوکیشن مپ:')
    tag_keywords = models.TextField(verbose_name='تگ keywords:')
    tag_description = models.CharField(max_length=250, verbose_name='تگ description:')
    bg_sm_homeSectionOne = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='عکس کوچک سکشن اول صفحه ایندکس:', help_text="resulotion(540*700) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_lg_homeSectionOne = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='عکس بزرگ سکشن اول صفحه ایندکس:', help_text="resulotion(540*700) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    title_top_homeSectionOne = tinymce_models.HTMLField(verbose_name='عنوان بالا سکشن اول صفحه ایندکس:')
    title_bottom_homeSectionOne = tinymce_models.HTMLField(verbose_name='عنوان پایین سکشن اول صفحه ایندکس:')
    info_homeSectionOne = tinymce_models.HTMLField(verbose_name='توضیحات سکشن اول صفحه ایندکس:')
    bg_homeSectionTwo = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='عکس کاور سکشن دوم صفحه ایندکس:', help_text="resulotion(720*750) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_contactUs = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='عکس کاور تماس با ما:', help_text="resulotion(1920*600) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    hour_work = tinymce_models.HTMLField(blank=True, verbose_name='توضیحات ساعت کاری:')
    copyright = tinymce_models.HTMLField(verbose_name='کپی رایت:')
    bg_404 = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='عکس خطای 404:', help_text="resulotion(400*300) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_500 = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='عکس خطای 500:', help_text="resulotion(400*300) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    
    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات وبسایت'

    def __str__(self):
        return self.title

@receiver(pre_save, sender=SettingsSite)
def delete_old_image_category(sender, instance, *args, **kwargs):
        if instance.pk:
            g_file = SettingsSite.objects.get(pk=instance.pk)
            if instance.logo and g_file.logo != instance.logo:
                g_file.logo.delete(False)
            if instance.bg_sm_homeSectionOne and g_file.bg_sm_homeSectionOne != instance.bg_sm_homeSectionOne:
                g_file.bg_sm_homeSectionOne.delete(False)
            if instance.bg_lg_homeSectionOne and g_file.bg_lg_homeSectionOne != instance.bg_lg_homeSectionOne:
                g_file.bg_lg_homeSectionOne.delete(False)
            if instance.bg_homeSectionTwo and g_file.bg_homeSectionTwo != instance.bg_homeSectionTwo:
                g_file.bg_homeSectionTwo.delete(False)
            if instance.bg_contactUs and g_file.bg_contactUs != instance.bg_contactUs:
                g_file.bg_contactUs.delete(False)
            if instance.bg_404 and g_file.bg_404 != instance.bg_404:
                g_file.bg_404.delete(False)
            if instance.bg_500 and g_file.bg_500 != instance.bg_500:
                g_file.bg_500.delete(False)


@receiver(pre_delete, sender=SettingsSite)
def service_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)
    instance.bg_sm_homeSectionOne.delete(False)
    instance.bg_lg_homeSectionOne.delete(False)
    instance.bg_homeSectionTwo.delete(False)
    instance.bg_contactUs.delete(False)
    instance.bg_404.delete(False)
    instance.bg_500.delete(False)