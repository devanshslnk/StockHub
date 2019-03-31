from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import User

def login_site(request):
    if(request.user.is_authenticated):
        if(request.user.is_superuser):
            return redirect("/admin_site/")
            # return render(request,"stockdata/admin_site.html",{"message":""})
        else:
            return redirect("/home/")
    login_resonse_message={}
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        if(User.objects.filter(email=email).exists()):

            user=authenticate(email=email,password=password)
            if(user is not None):

                login(request,user)
                if(user.is_superuser==True):
                    return redirect('/ownersite/')

                else:
                    return redirect('/home/')
            else:
                login_resonse_message['message']='incorrect password'
        else:
            login_resonse_message['message']='email doesnot exists'
    return render(request,'registeration/login.html',login_resonse_message)


def logout_site(request):
    if(request.user.is_authenticated):

        logout(request)
    return redirect("/");

def register_user(request):
    if(request.user.is_authenticated):
        if(request.user.is_superuser):
            print("super")
            # return redirect('/ownersite/')
        else:
            print("not super")
            # return redirect('/home/')
    register_response_message={}
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        contact_number=request.POST['contact_number']

        if not (User.objects.filter(email=email).exists()):
            print("user")
            user_create=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name,contact_number=contact_number)
            user=authenticate(email=email,password=password)
            login(request,user)
            return redirect("/home/")
        else:
            register_response_message['message']='Email already exists'
    return render(request,'registeration/login.html',register_response_message)






