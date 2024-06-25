from django.db import models
from .views import validate_image_extension
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from tinymce import models as tinymce_models
# Create your models here.

def upload_media_path(instance, filename):
    return f"Settings/{filename}"

class SettingsSite(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='title website:')
    logo = models.ImageField(upload_to=upload_media_path, validators=[validate_image_extension], verbose_name='logo:', help_text="resulotion(120*120)")
    link = models.URLField(blank=True, verbose_name='link website:')
    call = models.CharField(max_length=20, blank=True, verbose_name='call number:')
    mobile = models.CharField(max_length=20, blank=True, verbose_name='mobile number:')
    email = models.CharField(max_length=150, blank=True, verbose_name='email:')
    address = models.CharField(max_length=200, blank=True, verbose_name='address:')
    location_maps = models.CharField(max_length=600,blank=True, verbose_name='location map:')
    tag_keywords = models.TextField(verbose_name='tag keywords:')
    tag_description = models.CharField(max_length=250, verbose_name='tag description:')
    bg_slider_home = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='cover image slider index page:', help_text="resulotion(1920*1200) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_sm_homeSectionOne = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='small image section one index page:', help_text="resulotion(540*700) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_lg_homeSectionOne = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='large image section one index page:', help_text="resulotion(540*700) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    title_top_homeSectionOne = tinymce_models.HTMLField(verbose_name='title up image section one index page:')
    title_bottom_homeSectionOne = tinymce_models.HTMLField(verbose_name='title down image section one index page:')
    info_homeSectionOne = tinymce_models.HTMLField(verbose_name='description section one index page:')
    bg_homeSectionTwo = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='cover image section two index page:', help_text="resulotion(720*750) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_contactUs = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='cover image contact us:', help_text="resulotion(1920*600) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_footer = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='cover image footer:', help_text="resulotion(1920*700) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    hour_work = tinymce_models.HTMLField(blank=True, verbose_name='description hours work:')
    copyright = tinymce_models.HTMLField(verbose_name='copy right:')
    bg_404 = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='image error 404:', help_text="resulotion(400*300) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_500 = models.ImageField(upload_to=upload_media_path, blank=True, validators=[validate_image_extension], verbose_name='image error 500:', help_text="resulotion(400*300) , acception format: "'image = [jpg, png, bmp, gif, jpeg, svg]')
    
    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings website'

    def __str__(self):
        return self.title

@receiver(pre_save, sender=SettingsSite)
def delete_old_image_category(sender, instance, *args, **kwargs):
        if instance.pk:
            g_file = SettingsSite.objects.get(pk=instance.pk)

            if instance.logo and g_file.logo != instance.logo:
                g_file.logo.delete(False)

            if instance.bg_slider_home and g_file.bg_slider_home != instance.bg_slider_home:
                g_file.bg_slider_home.delete(False)

            if instance.bg_sm_homeSectionOne and g_file.bg_sm_homeSectionOne != instance.bg_sm_homeSectionOne:
                g_file.bg_sm_homeSectionOne.delete(False)

            if instance.bg_lg_homeSectionOne and g_file.bg_lg_homeSectionOne != instance.bg_lg_homeSectionOne:
                g_file.bg_lg_homeSectionOne.delete(False)

            if instance.bg_homeSectionTwo and g_file.bg_homeSectionTwo != instance.bg_homeSectionTwo:
                g_file.bg_homeSectionTwo.delete(False)

            if instance.bg_contactUs and g_file.bg_contactUs != instance.bg_contactUs:
                g_file.bg_contactUs.delete(False)

            if instance.bg_footer and g_file.bg_footer != instance.bg_footer:
                g_file.bg_footer.delete(False)

            if instance.bg_404 and g_file.bg_404 != instance.bg_404:
                g_file.bg_404.delete(False)

            if instance.bg_500 and g_file.bg_500 != instance.bg_500:
                g_file.bg_500.delete(False)


@receiver(pre_delete, sender=SettingsSite)
def service_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)
    instance.bg_slider_home.delete(False)
    instance.bg_sm_homeSectionOne.delete(False)
    instance.bg_lg_homeSectionOne.delete(False)
    instance.bg_homeSectionTwo.delete(False)
    instance.bg_contactUs.delete(False)
    instance.bg_footer.delete(False)
    instance.bg_404.delete(False)
    instance.bg_500.delete(False)