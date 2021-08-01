from django import forms
from django.forms.fields import CharField

class PostForm(forms.Form):
    text = forms.CharField()
    image = forms.ImageField()
    

