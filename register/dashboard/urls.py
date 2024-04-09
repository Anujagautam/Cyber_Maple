from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('files/', views.files, name='files'),
    path('notifications/', views.notifications, name='notifications'),
    path('chart/', views.chart, name='chart'),
    path('facial/', views.facial, name= 'facialdetection'),
    path('passport/', views.passport, name='passport'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('license/', views.license, name = 'license'),
    path('cdr/', views.cdr, name='cdr'),
    path('interrogation/', views.interrogation, name='interrogation'),    
]
