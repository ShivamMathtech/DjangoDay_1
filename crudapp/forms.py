from django import forms
from .models import LoginForms
class userForm(forms.ModelForm):
    class Meta:
        model=LoginForms
        fields=['name','password']
        