from datetime import datetime
from dateutil.relativedelta import relativedelta
from multiprocessing import context

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView, ListView,UpdateView,CreateView
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
            assignments = Assignments.objects.filter(assi_status=1).order_by('assi_daterenovation')
            #return self.model.objects.filter(cli_fkuser=self.request.user.id)
            # for ass in assignments:
            #     print(vars(ass))
            
            return render(request,'controlcuentas/index.html',{'assignments' : assignments, 'now': datetime.now()})
        else:
            path = f'/login'
            
        return redirect(to=path,) 
    
    

class Register(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'controlcuentas/user/register.html'
    
    def form_valid(self, form):
        form.instance.is_superuser = 0
        form.instance.is_active = 1
        form.instance.date_joined =  datetime.now()
        
        return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     message = f'Error: {form.instance.error_messages}'
    #     context = {
    #         'form': self.form_class,
    #         'message': message
    #     }
    #     return render(self.request,self.template_name,context)
    
    # message = ''
    # if request.method == 'POST':
    #     form = UserRegisterForm(data=request.POST)
    #     # form['is_superuser'] = 0
    #     # form['is_active'] = 1
    #     # form['date_joined'] = datetime.now()
    #     #return HttpResponse(vars(form))
    #     if form.is_valid():
    #         #form= form.cleaned_data["username"]
    #         user = form.save()
    #         #messages.success(request, f'El usuario: {username} a sido creado con exito!')
    #         #print(form.username)
    #         #pprint(form)
    #         return redirect(to='/')
    #     else:
    #         message = f'Los datos no est??n bien, verifiquelo de nuevo.'
        
    
    # return render(request,'controlcuentas/user/register.html', {'form': UserRegisterForm(),'message': message})

#Client
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
        
class AddClient(LoginRequiredMixin, CreateView):
    login_url = 'login'
    #model = Client
    form_class = ClientForm
    success_url = reverse_lazy('all-clients')
    template_name = 'controlcuentas/client/create.html'
    
    def form_valid(self, form):
        form.instance.cli_fkuser = self.request.user
        form.save()
        return super().form_valid(form)
class AllClients(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Client
    template_name = 'controlcuentas/client/all-clients.html'
    
    def get_queryset(self):
        return self.model.objects.filter(cli_fkuser=self.request.user.id)
    
class UpdateClient(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Client
    form_class = ClientForm
    template_name = 'controlcuentas/client/update.html'
    success_url = reverse_lazy('all-clients')
    


#Asignments
class AllAssignments(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Assignments
    template_name = 'controlcuentas/assignment/all.html'
    
    def get_queryset(self):
        return self.model.objects.filter(assi_fkuser=self.request.user.id)
    

class AddAssignment(LoginRequiredMixin,CreateView):
    login_url = 'login'
    form_class = AssignmentsForm
    template_name = 'controlcuentas/assignment/create.html'
    success_url = reverse_lazy('all-assignments')
    
    def form_valid(self, form):
        form.instance.assi_daterenovation = form.instance.assi_datepurchase + relativedelta(months=1)
        form.instance.assi_status = 1
        form.instance.assi_fkuser = self.request.user
        return super().form_valid(form)
    
class ViewAssignment(LoginRequiredMixin, View):
    model = Assignments
    login_url = 'login'
    template_name = 'controlcuentas/assignment/view.html'
    
    def get_queryset(self):
        return self.model.objects.get(assi_id=self.kwargs.get('pk'))
    
    def get(self, request, *args, **kwargs):
        context = {
            'assi': self.get_queryset()
        }
        return render(request,self.template_name,context)
    

class UpdateAssignment(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Assignments
    form_class = AssignmentsForm
    template_name = 'controlcuentas/assignment/update.html'
    success_url = reverse_lazy('all-assignments')
    
    def form_valid(self, form):
        form.instance.assi_daterenovation = form.instance.assi_datepurchase + relativedelta(months=1)
        return super().form_valid(form)
    
    # def get_queryset(self):
    #     return  self.model.objects.get(assi_id=self.kwargs.get('pk'))
        #data.assi_datepurchase = data.assi_datepurchase.strftime('%m/%d/%y')
        # print(data.assi_datepurchase)
        # return data
    
    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object();
    #     pprint(self.object.assi_datepurchase)
    #     print(self.object.assi_datepurchase)
    #     self.object.assi_datepurchase = self.object.assi_datepurchase.strftime('%m-%d-%Y')
    #     # print(vars(self.object))
        
    #     # print(datetime.strftime(self.object.assi_datepurchase,'%m-%d-%Y'))
    #     return super().dispatch(request, *args, **kwargs)
        



#Account
class AllAccount(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Account
    template_name = 'controlcuentas/account/all.html'
    
    def get_queryset(self):
        return self.model.objects.filter(acc_fkuser=self.request.user.id)
    
class CreateAccount(LoginRequiredMixin,CreateView):
    login_url = 'login'
    form_class = AccountForm
    template_name = 'controlcuentas/account/create.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.acc_fkuser = self.request.user
        return super().form_valid(form)
    
class ViewAccount(LoginRequiredMixin, View):
    login_url = 'login'
    model = Account
    template_name = 'controlcuentas/account/view.html'
    
    def get_queryset(self):
        return self.model.objects.get(acc_id=self.kwargs.get('pk'))
    
    def get(self, request, *args, **kwargs):
        context = {
            'account': self.get_queryset()
        }
        return render(request,self.template_name,context)
    
class UpdateAccount(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Account
    form_class = AccountForm
    template_name = 'controlcuentas/account/update.html'
    success_url = reverse_lazy('all-assignments')