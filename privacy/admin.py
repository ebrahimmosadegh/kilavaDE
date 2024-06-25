from django.contrib import admin

from .models import Datenschutz, Impressum

# Register your models here.
admin.site.register(Datenschutz)
admin.site.register(Impressum)
