from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import *
from modules.controlcuentas.models import *
from modules.controlcuentas.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import json
from pprint import pprint

# Create your views here.

def index(request):
    return render(request,'controlcuentas/index.html',{'nombre' : [1,2,], })

def view(request,id):
    return HttpResponse(id)
    return render(request,'controlcuentas/view.html')

def agregar_cuenta(request):
    
    if request.method == 'POST':
        cliente = ClientForm(request.POST)
        if(cliente.is_valid()):
            cliente = cliente.save()
            print(type(cliente.cli_id))
            return redirect('/controlcuentas/view/'+str(cliente.cli_id))
                
        else:
            return HttpResponse("no")
            
    
    return render(request,'controlcuentas/agregar-cuenta.html',{'form': ClientForm()})

def register(request):
    message = ''
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        # form['is_superuser'] = 0
        # form['is_active'] = 1
        # form['date_joined'] = datetime.now()
        #return HttpResponse(vars(form))
        if form.is_valid():
            #form= form.cleaned_data["username"]
            user = form.save()
            #messages.success(request, f'El usuario: {username} a sido creado con exito!')
            #print(form.username)
            #pprint(form)
            return redirect(to='/')
        else:
            message = f'Los datos no están bien, verifiquelo de nuevo.'
        
    
    return render(request,'controlcuentas/user/register.html', {'form': UserRegisterForm(),
                                                                'message': message})
