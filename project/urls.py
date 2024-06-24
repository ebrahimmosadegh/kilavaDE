"""
URL configuration for kilavair project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from kilavair import settings
from kilavair.views import home_page, header, footer, handler404, handler500
from .sitemaps import ArticleSitemap, StaticSitemap, HomeSitemap
from django.contrib.sitemaps.views import sitemap, index
from .robots import robots_txt


sitemaps = {
    'services':ArticleSitemap,
    'homeSiteMaps':HomeSitemap,
    'static':StaticSitemap #add StaticSitemap to the dictionary
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('', include('contact.urls', namespace='Contact')),
    path('', include('about.urls', namespace='About')),
    path('', include('services.urls', namespace='Services')),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', sitemap, {'sitemaps': sitemaps,'template_name': 'seo/custom_sitemap.html'}, 
    name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt),
]

# handle 404 and 500 error
handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    # add root statice files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)