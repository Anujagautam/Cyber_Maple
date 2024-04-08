from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('login/' , views.login_page, name= 'login_page'),
    
]
