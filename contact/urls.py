from django.urls import path

from .views import contact

app_name = 'Contact'

urlpatterns = [
    path('contact-us', contact, name='contact-us'),
]