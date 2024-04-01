
# views.py
from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def enemy_detection(request):
    return render(request, 'dashboard/enemy_detection.html')

def notifications(request):
    return render(request, 'dashboard/notifications.html')
