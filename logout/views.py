from django.shortcuts import render

# Create your views here.
def logout(request):
    return render (request , 'logout/logout_first.html')