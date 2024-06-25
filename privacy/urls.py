from django.urls import path

from .views import datenschutz, impressum

app_name = 'Privacy'

urlpatterns = [
    path('datenschutz/', datenschutz, name='datenschutz'),
    path('impressum/', impressum, name='impressum'),
]