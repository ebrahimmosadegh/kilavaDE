from django.urls import path

from .views import about

app_name = 'About'

urlpatterns = [
    path('about-us/', about, name='about-us'),
]