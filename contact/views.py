import json
import requests
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from project import settings
from project.views import settings as settings_website
from .forms import CreateContactForm
from .models import ContactUs


def contact(request):
    site_key_captcha = settings.GOOGLE_RECAPTCHA_SITE_KEY
    secret_key_captcha = settings.GOOGLE_RECAPTCHA_SECRET_KEY
    contact_form = CreateContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            fullname = contact_form.cleaned_data.get('fullname')
            email = contact_form.cleaned_data.get('email')
            call = contact_form.cleaned_data.get('call')
            subject = contact_form.cleaned_data.get('subject')
            text = contact_form.cleaned_data.get('text')

            captcha_token = request.POST.get("g-recaptcha-response")
            cap_url = "https://www.google.com/recaptcha/api/siteverify"
            cap_secret = secret_key_captcha
            cap_data = {"secret": cap_secret, "response": captcha_token}
            cap_server_response = requests.post(url=cap_url, data=cap_data)
            cap_json = json.loads(cap_server_response.text)
            if cap_json['success'] == False:
                messages.error(request, "please check I'm not a robot ", extra_tags='contact_message_error')
            else:
                ContactUs.objects.create(fullname=fullname,call=call, email=email, subject=subject, text=text, is_read=False)
                contact_form = CreateContactForm()
                messages.success(request, "Your message has been successfully sent..", extra_tags='contact_message')
        else:
            contact_form = CreateContactForm()

    context = {
        'site_key_captcha': site_key_captcha,
        'contact_form': contact_form,
        'setting': settings_website(),
    }

    return render(request, 'contact.html', context)
