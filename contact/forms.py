from django import forms
from contact.models import *

class contact_form(forms.ModelForm):
    class Meta:
        model = contato
        fields = '__all__'