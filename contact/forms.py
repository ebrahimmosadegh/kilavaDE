from django import forms
from django.core import validators
from .models import ContactUs

class CreateContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name and Family', 'type': 'text','name':'name' ,'id':'name', 'data-error':'please enter Name and Family..'}),
        validators=[
            validators.MaxLengthValidator(200, 'your Data can not more 200 characters!')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'type': 'email','name':'email', 'id':'email', 'data-error':'Email is required..'}),
        validators=[
            validators.MaxLengthValidator(100, 'your Email can not more 100 characters!')
        ]
    )

    call = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Call Number', 'type': 'text','name':'phone_number', 'id':'phone_number' , 'data-error': 'You forgot the Contact Number!'}),
        validators=[
            validators.MaxLengthValidator(50, 'your Number can not more 50 characters!')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'type': 'text', 'name':'msg_subject' , 'id':'msg_subject' , 'data-error':'please enter your Subject..'}),
        validators=[
            validators.MaxLengthValidator(200, 'your Subject can not more 200 characters!')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'your Text', 'name':'message', 'id':'message', 'cols':'30', 'rows':'10', 'data-error':'your Text is blank!',
                   }),
    )


