from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import AboutUs

# Create your views here.
def about(request):
    try:
        return render(request, 'about-us.html', {'aboutquery': AboutUs.objects.last()})
    except ObjectDoesNotExist:
        pass
    