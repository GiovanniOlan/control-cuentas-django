from datetime import datetime
from multiprocessing import context

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from modules.controlcuentas.models import *
from modules.controlcuentas.forms import *
from django.contrib import messages
from pprint import pprint
from django.contrib.auth.decorators import login_required

# Create your views here.

class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        path = 'index.html'
        if request.user.is_authenticated:
            return render(request,'controlcuentas/index.html',{'nombre' : [1,2,], })
        else:
            path = f'/login'
            
        return redirect(to=path,) 


class View(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    #login_url = 'login'
    template_name = 'controlcuentas/view.html'
class AgregarCliente(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'controlcuentas/agregar-cliente.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ClientForm
        return context
        
        
            #return render(request,'controlcuentas/agregar-cuenta.html',{'form': ClientForm()})
    def post(self, request, *args, **kwargs):
        data_client = request.POST.copy()
        data_client['cli_fkuser'] = request.user.id
        cliente = ClientForm(data_client)
        if(cliente.is_valid()):
            #return HttpResponse(cliente)
            cliente = cliente.save()
            print(type(cliente.cli_id))
            return redirect(to='view')
        else:
            return HttpResponse('Algo salio mal')
                
            
    

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
    
def all_clients(request):
    
    
    
    return render(request,'controlcuentas/client/all-clients.html')
