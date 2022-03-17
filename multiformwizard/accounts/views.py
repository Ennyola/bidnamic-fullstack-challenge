from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    '''
    Function to log in a user
    '''
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        redirect_next = request.POST.get("next")
        user = authenticate(username=username, password=password)
        #Authentication credentials are valid and the user exists
        if user is not None:
            login(request, user)
            #redirect to specific page if redirect_next is a valid url
            if len(redirect_next) > 0 and redirect_next is not None:
                return redirect(redirect_next)
            return redirect("index")
        #Authentication credentials are invalid
        messages.error(request, "Invalid Username or Password")
    return render(request, "accounts/login.html")


def signup(request):
    '''
    Function for user signup
    '''
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        rt_password = request.POST.get("rtpassword", None)
        #return error if passwords do not match
        if password != rt_password:
            messages.error(request, "Password do not match")
        else:
            #creates a user using just the username if user does not exist else return error
            user, created = User.objects.get_or_create(username=username)
            if created:
                #set user password and update user
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect("index")
            messages.error(request, "User Already Exists")
    return render(request, "accounts/signup.html")


def logout_view(request):
    '''
    Function to log out a user
    '''
    logout(request)
    return redirect("accounts:login")
