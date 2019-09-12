from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse

def login(request):
    return render(request,'login.html')
    #return HttpResponse('')

#def login(request):
 #   return render(request, 'login.html')
# Create your views here.
