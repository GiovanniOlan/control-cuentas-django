from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from modules.controlcuentas.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        
    



