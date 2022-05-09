from datetime import datetime
from multiprocessing import context

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView, ListView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from modules.controlcuentas.models import *
from modules.controlcuentas.forms import *
from django.contrib import messages
from pprint import pp, pprint
from django.urls import reverse_lazy

# Create your views here.

class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        path = 'index.html'
        if request.user.is_authenticated:
            return render(request,'controlcuentas/index.html',{'nombre' : [1,2,], })
        else:
            path = f'/login'
            
        return redirect(to=path,) 
    
    

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
        
    
    return render(request,'controlcuentas/user/register.html', {'form': UserRegisterForm(),'message': message})


class ViewClient(LoginRequiredMixin, View):
    model = Client
    login_url = 'login'
    template_name = 'controlcuentas/client/view.html'
    
    def get_queryset(self):
        return self.model.objects.get(cli_id=self.kwargs.get('pk'))
    
    def get(self, request, *args, **kwargs):
        context = {
            'client': self.get_queryset()
        }
        return render(request,self.template_name,context)
        
        
    
class AddClient(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'controlcuentas/client/create.html'
    extra_context = {'form': ClientForm}
    
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
class AllClients(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Client
    template_name = 'controlcuentas/client/all-clients.html'
    
    def get_queryset(self):
        return Client.objects.filter(cli_fkuser=self.request.user.id)
    
class UpdateClient(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Client
    form_class = ClientForm
    template_name = 'controlcuentas/client/update.html'
    success_url = reverse_lazy('all-clients')
    
