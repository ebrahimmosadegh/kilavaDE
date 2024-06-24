from django.http import Http404
from django.shortcuts import render
from services.models import Services
from django.core.exceptions import ObjectDoesNotExist
from tools.models import SettingsSite

def settings():
    try:
        setting=  SettingsSite.objects.last()
        return setting
    except ObjectDoesNotExist:
        None

def context():
    try:
        services = Services.objects.all()
        query ={ 
            'services': services,
            'setting': settings()
        }
        return query
    except ObjectDoesNotExist:
        pass


def header(request):
    return render(request, 'shared/header.html', context())


def footer(request):
    return render(request, 'shared/footer.html', context())


def home_page(request):
    return render(request, 'index.html', context())


def handler404(request, exception):

    return render(request, 'Error/404.html', {'setting': settings()}, status=404)

def handler500(request):
    return render(request, 'Error/500.html', {'setting': settings()}, status=500)