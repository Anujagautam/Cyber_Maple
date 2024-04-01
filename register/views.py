from django.shortcuts import render , redirect

from django.contrib.auth import authenticate, login, logout


# Create your views here.

def regi(request):
    return render(request , 'register/register_first.html')


