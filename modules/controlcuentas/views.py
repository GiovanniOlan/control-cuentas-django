from django.http import HttpResponse
from django.shortcuts import *
from modules.controlcuentas.models import *
from modules.controlcuentas.forms import *
import json

# Create your views here.

def index(request):
    
    diccionario = {'nombre' : [1,2,3,4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,], }
    return render(request,'controlcuentas/index.html',diccionario)

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
            
    

    form_class = ClientForm
    context = {'form': form_class}
    return render(request,'controlcuentas/agregar-cuenta.html',context)
