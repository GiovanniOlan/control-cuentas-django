from django.forms import ModelForm
from modules.controlcuentas.models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
        


