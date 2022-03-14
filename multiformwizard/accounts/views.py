from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def login_view(request):
    if request.method=="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
             messages.error(request, "Invalid Username or Password")
             return redirect("accounts:login")
    return render(request,"accounts/login.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        rt_password = request.POST.get("rtpassword",None)
        
        if password != rt_password:
            messages.error(request, "Password do not match")
            return redirect("accounts:signup")
        user,created= User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "User Already Exists")
    return render(request,"accounts/signup.html")

def logout_view(request):
    logout(request)
    return redirect("accounts:login")
    