from django.urls import path
from . import views
from modules.controlcuentas.views import *

#For Folder static 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('',Index.as_view(), name='index'),
    path('index', Index.as_view(), name='index'),
    path('register',views.register, name='register'),
    #Client
    path('view/<pk>', ViewClient.as_view(), name='view_client'),
    path('add-client',AddClient.as_view(), name='add-client'),
    path('client/all',AllClients.as_view(), name='all-clients'),
    path('client/update/<pk>',UpdateClient.as_view(), name='update-client'),
    
    
    #Assignments
    path('assignments/',AllAssignments.as_view(), name='all-assignments'),
    path('assignments/create',AddAssignment.as_view(), name='add-assignment'),
    path('assignments/view/<pk>', ViewAssignment.as_view(), name='view_assignment'),
    path('assignments/update/<pk>',UpdateAssignment.as_view(), name='update_assignment'),
    
    #Accounts
    path('account/all',AllAccount.as_view(), name='all_accounts'),
    path('account/create', CreateAccount.as_view(), name='create_account'),
    path('account/view/<pk>', ViewAccount.as_view(), name='view_account'),
    path('account/update/<pk>',UpdateAccount.as_view(), name='update_account'),
    
    
    
]