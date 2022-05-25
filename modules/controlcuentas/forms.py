from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from modules.controlcuentas.models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['cli_fkuser']
        
class AssignmentsForm(ModelForm):
    class Meta:
        model = Assignments
        fields = '__all__'
        exclude = ['assi_fkuser','assi_daterenovation','assi_status']
        
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        

        
    



