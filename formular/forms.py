from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
#    name = forms.CharField(required=True)
    name = forms.CharField(max_length=100)
#    email = forms.EmailField(required=True)
    email = forms.CharField(validators=[EmailValidator()])
#    phone = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
