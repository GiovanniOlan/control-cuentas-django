from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Index')

def contact(request):
    return HttpResponse('Contactanos')