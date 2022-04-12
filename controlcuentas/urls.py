from django.urls import path
from . import views

#For Folder static 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('',views.index, name='index'),
]