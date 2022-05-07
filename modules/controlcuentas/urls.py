from django.urls import path
from . import views
from modules.controlcuentas.views import *

#For Folder static 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('',Index.as_view(), name='index'),
    path('index', Index.as_view(), name='index'),
    path('view', View.as_view(), name='view'),
    path('agregar-cliente',AgregarCliente.as_view(), name='agregar-cliente'),
    path('register',views.register, name='register'),
    path('all-clients',views.all_clients, name='all-clients'),
]