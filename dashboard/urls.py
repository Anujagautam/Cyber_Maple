from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enemy_detection/', views.enemy_detection, name='enemy_detection'),
    path('notifications/', views.notifications, name='notifications'),
    path('chart/', views.chart, name='chart'),

    # Add more URL patterns as needed
]
