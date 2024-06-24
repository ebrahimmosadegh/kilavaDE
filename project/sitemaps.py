from django.contrib.sitemaps import Sitemap
from services.models import Services
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3
    protocol = 'http'
    limit = 50000

    def items(self):
        service = Services.objects.all()
        return service

    def location(self,obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.timestamp


#You can also add static pages such as home to your dynamic Django sitemap
class HomeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3
    protocol = 'http'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


#You can also add static pages such as /contact or /about to your dynamic Django sitemap
class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.2
    protocol = 'http'

    def items(self):
        return ['About:about-us', 'Contact:contact-us']

    def location(self, item):
        return reverse(item)