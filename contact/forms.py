from django import forms
from django.core import validators
from .models import ContactUs

class CreateContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی', 'type': 'text','name':'name' ,'id':'name', 'data-error':'لطفا نام و نام خانوادگی خود را وارد نمایید'}),
        validators=[
            validators.MaxLengthValidator(200, 'مشخصات شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'type': 'email','name':'email', 'id':'email', 'data-error':'ایمیل الزامی میباشد'}),
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')
        ]
    )

    call = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'شماره تماس', 'type': 'text','name':'phone_number', 'id':'phone_number' , 'data-error': 'شماره تماس را فراموش نموده اید'}),
        validators=[
            validators.MaxLengthValidator(50, 'شماره تماس شما نمیتواند بیشتر از 50 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان', 'type': 'text', 'name':'msg_subject' , 'id':'msg_subject' , 'data-error':'لطفا عنوان را وارد نمایید'}),
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'متن سخنان شما', 'name':'message', 'id':'message', 'cols':'30', 'rows':'10', 'data-error':'متن سخنان شما خالی میباشد',
                   }),
    )


