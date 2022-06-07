from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from modules.controlcuentas.models import *


class DateInput(forms.DateInput):
    input_type = 'date'
    
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
        widgets = {
            'assi_datepurchase': DateInput()
        }
        
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['acc_fkuser']       
    



