from django.contrib.auth.models import User
from django.forms import forms, ModelForm
from django import forms

from .models import Postes


class RegUser(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
class LogUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class NewPost(ModelForm):
    class Meta:
        model = Postes
        fields = ['auto', 'problem', 'date']