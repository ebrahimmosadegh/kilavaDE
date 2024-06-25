from django.shortcuts import render, get_object_or_404

from project.views import settings
from .models import Services, Gallery

# Create your views here.


def service(request, slug):
    service = get_object_or_404(Services, slug=slug)
    galleries = Gallery.objects.filter(service_id=service.pk)
    context = {
        'service': service,
        'galleries': galleries,
        'setting': settings(),
    }
    return render(request, 'service.html', context)
