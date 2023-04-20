from django import forms
from contact.models import *

class contact_form(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, required=True, strip=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100,min_length=5, required=True)
    message = forms.CharField(max_length=500, required=True, min_length=10)