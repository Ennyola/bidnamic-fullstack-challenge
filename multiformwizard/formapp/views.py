from django.shortcuts import render
from .models import Account
# Create your views here.

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
        
        print(d_o_b.split('-')[0])
        # account =  Account(title=title,first_name=first_name,surname=surname,d_o_b=d_o_b,address=address,telephone=telephone,bidding_settings=bd_settings)
        # account.save()
    
    return render(request, "formapp/customerSubmitForm.html")