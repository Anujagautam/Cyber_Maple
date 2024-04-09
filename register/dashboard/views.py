
# views.py
from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def files(request):
    return render(request, 'dashboard/files.html')

def notifications(request):
    return render(request, 'dashboard/notifications.html')

def chart(request):
    return render(request, 'dashboard/chart.html')

def facial(request):
    return render(request, 'dashboard/facialdetection.html')

def passport(request):
    return render(request, 'dashboard/passport.html')

def vehicle(request):
    return render(request, 'dashboard/vehicle.html')

def license(request):
    return render(request, 'dashboard/license.html')

def cdr(request):
    return render(request, 'dashboard/cdr.html')

def interrogation(request):
    return render(request, 'dashboard/interrogation.html')



