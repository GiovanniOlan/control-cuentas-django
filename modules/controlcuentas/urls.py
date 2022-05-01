from django.urls import path
from . import views

#For Folder static 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('',views.index, name='index'),
    path('view/<id>',views.view, name='view'),
    path('agregar-cuenta',views.agregar_cuenta, name='agregar-cuenta')
]