from django.shortcuts import render , redirect

from django.contrib.auth import authenticate, login, logout

from register.models import  Person

def regi(request):


    if request.method == "POST":
        print("Login Page Call")
        full_name = request.POST['fullName']
        usern_name = request.POST['username']
        email = request.POST['email']
        phone_no= request.POST['phoneNumber']
        password = request.POST['password']
        con_password = request.POST['confirmPassword']
        print(full_name ,usern_name , email ,phone_no ,password, con_password )
        insert = Person(full_name=full_name , usern_name=usern_name , email=email , password = password , con_password = con_password ,phone_no=phone_no )
        insert.save()
        print("Data Save Inside the PErson Table Tb")
        return redirect('login:login_page')



    return render(request , 'register/register_first.html')


