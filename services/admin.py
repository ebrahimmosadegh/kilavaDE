from django.contrib import admin
from .models import Services, Gallery

# Register your models here.

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'image_tag']
    inlines = [GalleryInline]
    list_per_page = 10

    class Meta:
        model = Services

admin.site.register(Services, ServiceAdmin)
# Register your models here.
