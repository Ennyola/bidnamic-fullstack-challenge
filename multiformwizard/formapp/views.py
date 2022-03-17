import imp
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserApplication
# Create your views here.


@login_required
def index(request):
    if request.method=="POST":  
        title=request.POST.get("title",None)
        first_name=request.POST.get("firstname",None)
        surname=request.POST.get("surname",None)
        d_o_b=request.POST.get("d_o_b",None)
        address=request.POST.get("address",None)
        telephone=request.POST.get("telephone",None)
        bd_settings=request.POST.get("bd-settings",None)
        google_id=request.POST.get("google_id",None)
        company_name = request.POST.get("company_name",None)
       
        if UserApplication.objects.filter(google_id=google_id).exists():
            messages.error(request, "An Application with that GOOGLE ID already exists")
        else:
            UserApplication.objects.create(title=title,first_name=first_name,surname=surname,d_o_b=d_o_b,company_name=company_name,address=address,telephone=telephone,bidding_settings=bd_settings.upper(),google_id=google_id)
            return redirect("applications")
    
    return render(request, "formapp/customerSubmitForm.html")

@login_required
def show_applications(request):
    applications = UserApplication.objects.all()
    context={
        "applications":applications
    }
    
    return render(request, "formapp/showapplications.html",context)

@login_required
def delete_application(request,id):
    application = UserApplication.objects.get(id=id)
    application.delete()
    return redirect("applications")