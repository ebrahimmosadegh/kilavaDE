from django.urls import path

from .views import service

app_name = 'Services'

urlpatterns = [
    path('service/<slug:slug>', service, name='service'),
]