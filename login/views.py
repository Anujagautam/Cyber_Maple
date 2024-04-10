from django.shortcuts import render , redirect

# Create your views here.
from login.models import Person_login
from register.models import Person
from django.http import HttpResponse
def login_page(request):

    if request.method == "POST":
        print("yes I am Dash Board")

        full_name = request.POST['Username']
        password = request.POST['password_fill']

        print(full_name , password)
        # insert_data = Person_login(full_name = full_name , password = password)
        # insert_data.save()
        # return redirect("dashboard:dashboard_page")

        Person_regi_data = Person.objects.all()
        

        for data in Person_regi_data:
            register_username_data = data.usern_name
            register_pasword_data = data.password
            print("Login Page Data", full_name ,password )
            print("register Page Data",register_username_data, register_pasword_data)
            if (str(register_username_data)==str(full_name) ) and (str(password)==str(register_pasword_data)):
                print("Now Call I am ")
                return redirect('dashboard:dashboard')
                

               
    else:
        return render(request , 'login/login_first.html')
            


    return render(request , 'login/login_first.html')
    

