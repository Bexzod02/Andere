from dataclasses import fields
from pyexpat import model
from django import forms
from .models import GetInTouch, Subscribe

class Contactform(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(Contactform, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name    
    
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields=['email']
    
