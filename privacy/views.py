from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Datenschutz, Impressum

# Create your views here.
def datenschutz(request):
    try:
        return render(request, 'datenschutz.html', {'datenschutz': Datenschutz.objects.last()})
    except ObjectDoesNotExist:
        pass

def impressum(request):
    try:
        return render(request, 'impressum.html', {'impressum': Impressum.objects.last()})
    except ObjectDoesNotExist:
        pass